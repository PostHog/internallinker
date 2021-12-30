import os
import yaml
import sys
import re
import glob
import json
import collections
import frontmatter
from pathlib import Path
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'generated-posts'
ALLOWED_EXTENSIONS = {'md','mdx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def glob_filetypes(root_dir, *patterns):
    return [path
            for pattern in patterns
            for path in glob.glob(os.path.join(root_dir, pattern))]

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist("file")
        for file in files:
            if file.filename == '':
                flash('No selected file')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if request.form.get('topics'):
            topicSupport=True
        else:
            topicSupport=False

        generate_keywords(topicSupport)
        duplicateKeywords = duplicate_check()
        linkOutput = generate_links(duplicateKeywords)

        return render_template('index.html', linkOutput=linkOutput, duplicateKeywords=duplicateKeywords)

def generate_keywords(topicSupport):
    keywords = ''
    blogText = ''
    keywordAssociations = {}
    linkId = 1
    for file in sorted(glob_filetypes(app.config['UPLOAD_FOLDER'], '*.md', '*.mdx')):
        with open(os.path.join(os.getcwd(), file), 'r') as f:
            fileName = Path(os.path.splitext(f.name)[0]).stem
            frontMatter, blogText = frontmatter.parse(f.read())
            try:
                frontMatter["topics"]
            except:
                frontMatter["topics"] = []
            try:
                frontMatter["keywords"]
            except:
                frontMatter["keywords"] = []
            if topicSupport:
                keywords = frontMatter["topics"]+frontMatter["keywords"]
            else:
                keywords = frontMatter["keywords"]
            for keyword in keywords:
                keywordAssociations.update({linkId : {}})
                linkDetails = {fileName : keyword}
                keywordAssociations[linkId].update(linkDetails)
                linkId += 1
    with open(app.config['UPLOAD_FOLDER'] + "/keywordAssociations.json", "w") as outfile:
        json.dump(keywordAssociations, outfile)
    return

def duplicate_check():
    jsonFile = open(app.config['UPLOAD_FOLDER'] + '/keywordAssociations.json')
    keywordAssociations = json.load(jsonFile)
    keywordList = []
    for key, value in keywordAssociations.items():
                for url, linkedKeyword in value.items():
                    keywordList.append(linkedKeyword)  
    duplicateKeywords = [item for item, count in collections.Counter(keywordList).items() if count > 1]
  
    return duplicateKeywords

def generate_links(duplicateKeywords):
    jsonFile = open(app.config['UPLOAD_FOLDER'] + '/keywordAssociations.json')
    keywordAssociations = json.load(jsonFile)

    for file in sorted(glob_filetypes(app.config['UPLOAD_FOLDER'], '*.md', '*.mdx')):
        with open(os.path.join(os.getcwd(), file), 'r+') as f:
            frontMatter, blogText = frontmatter.parse(f.read())
            for key, value in keywordAssociations.items():
                for url, linkedKeyword in value.items():
                    # don't link the existing file to itself
                    currentUrl = Path(os.path.splitext(f.name)[0]).stem
                    if url != currentUrl:
                        newText = "["+linkedKeyword+"]("+url+")"
                        # check the keywords have a space before/after to prevent this problem: [keyword](link)s
                        # todo: this is hideous hardcoding, refactor if it bothers you!
                        blogText = blogText.replace(" "+linkedKeyword+" "," "+newText+" ")
                        blogText = blogText.replace(" "+linkedKeyword+","," "+newText+",")
                        blogText = blogText.replace(" "+linkedKeyword+";"," "+newText+";")
                        blogText = blogText.replace(" "+linkedKeyword+'.'," "+newText+'.')
                        # check if new file has created links inside links, in which case - stop
                        if "[[" not in blogText:
                            markdownContent = "---\n"+yaml.dump(frontMatter) + "---\n" + blogText
                            f.truncate(0)
                            f.seek(0) #avoids weird characters at the start
                            f.write(markdownContent)
    return(keywordAssociations)
