import os
import yaml
import sys
import re
import glob
import json
from pathlib import Path
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'generated-posts'
ALLOWED_EXTENSIONS = {'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        generate_keywords()
        return redirect(url_for('upload_file', name=filename))

def generate_keywords():
    keywords = ''
    blogText = ''
    keywordAssociations = {}

    # Grab each md post in the blog folder and get the keywords from the YAML in the markdown file
    linkId = 1
    for file in glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*.md')):
        with open(os.path.join(os.getcwd(), file), 'r') as f:
            fileName = Path(os.path.splitext(f.name)[0]).stem
            frontMatter, blogText = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]
            keywords = frontMatter["keywords"]
            for keyword in keywords:
                keywordAssociations.update({linkId : {}})
                linkDetails = {fileName : keyword}
                keywordAssociations[linkId].update(linkDetails)
                linkId += 1
                print(keywordAssociations)
    with open(app.config['UPLOAD_FOLDER'] + "/keywordAssociations.json", "w") as outfile:
        json.dump(keywordAssociations, outfile)
    generate_links()
    return

def generate_links():
    jsonFile = open(app.config['UPLOAD_FOLDER'] + '/keywordAssociations.json')
    keywordAssociations = json.load(jsonFile)

    for file in glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*.md')):
        with open(os.path.join(os.getcwd(), file), 'r+') as f:
            frontMatter, blogText = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]
            for key, value in keywordAssociations.items():
                for url, linkedKeyword in value.items():
                    newText = "["+linkedKeyword+"]("+url+")"
                    blogText = blogText.replace(linkedKeyword,newText)
                    markdownContent = "---\n"+yaml.dump(frontMatter) + "---\n" + blogText
            # replace the file contents
            f.truncate(0)
            f.seek(0) #avoids weird characters at the start
            f.write(markdownContent)
    return
