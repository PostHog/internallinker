import yaml
import json
import os
import glob
import re
# CONFIGURATION
# Set path to the folder containing the blog posts
#todo: make this re-use the config from generate-keywords.py
path = 'blog'


jsonFile = open('keywordAssociations.json')
keywordAssociations = json.load(jsonFile)

for file in glob.glob(os.path.join(path, '*.md')):
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