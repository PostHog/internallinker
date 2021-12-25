import yaml
import sys
import os
import glob

# CONFIGURATION
# Set path to the folder containing the blog posts
path = 'blog'

# Read through a list of post URLs and their keywords
keywordAssociations = {
    "/ceo-diary-3" : ["cancer", "0 to 1"],
    "/ceo-diary-2" : ["founder break up"],
    "/series-b" : ["fundraise"]
}

# Grab a blog post and get the keywords from the YAML in the markdown file
keywords = ''
blogText = ''

for filename in glob.glob(os.path.join(path, '*.md')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
        frontMatter, blogText = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]
        keywords = frontMatter["keywords"].split(",")
        print(keywords)
# Get the file path
filepath = os.path.splitext("example-post.md")[0]

# Save these keywords into a list
for keyword in keywords:
    keywordAssociations[filepath] = [keyword]

# Insert link whenever a keyword is found

for key, value in keywordAssociations.items():
    for i in value:
        newText = "["+i+"]("+key+")"
        blogText = blogText.replace(i,newText)

print(blogText)