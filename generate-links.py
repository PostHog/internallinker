import yaml
import json
import os
import glob

# CONFIGURATION
# Set path to the folder containing the blog posts
#todo: make this re-use the config from generate-keywords.py
path = 'blog'


jsonFile = open('keywordAssociations.json')
keywordAssociations = json.load(jsonFile)
print(keywordAssociations)

for file in glob.glob(os.path.join(path, '*.md')):
    with open(os.path.join(os.getcwd(), file), 'r') as f:
        frontMatter, blogText = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]

        for key, value in keywordAssociations.items():
            print(keywordAssociations)
#todo: fix this loop
            for i in value:
                newText = "["+i+"]("+key+")"
                blogText = blogText.replace(i,newText)
