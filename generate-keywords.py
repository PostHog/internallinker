import yaml
import sys
import os
import glob
import json
from pathlib import Path


# CONFIGURATION
# Set path to the folder containing the blog posts
path = 'blog'


keywords = ''
blogText = ''
keywordAssociations = {}

# Grab each md post in the blog folder and get the keywords from the YAML in the markdown file

linkId = 1
for file in glob.glob(os.path.join(path, '*.md')):
    with open(os.path.join(os.getcwd(), file), 'r') as f:
        fileName = Path(os.path.splitext(f.name)[0]).stem
        frontMatter, blogText = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]
        keywords = frontMatter["keywords"].split(",")
        for keyword in keywords:
            keywordAssociations.update({linkId : {}})
            linkDetails = {fileName : keyword}
            keywordAssociations[linkId].update(linkDetails)
            linkId += 1
            print(keywordAssociations)
with open("keywordAssociations.json", "w") as outfile:
    json.dump(keywordAssociations, outfile)