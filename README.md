```
.___        __                             .__  .____    .__        __                 
|   | _____/  |_  ___________  ____ _____  |  | |    |   |__| ____ |  | __ ___________ 
|   |/    \   __\/ __ \_  __ \/    \\__  \ |  | |    |   |  |/    \|  |/ // __ \_  __ \
|   |   |  \  | \  ___/|  | \/   |  \/ __ \|  |_|    |___|  |   |  \    <\  ___/|  | \/
|___|___|  /__|  \___  >__|  |___|  (____  /____/_______ \__|___|  /__|_ \\___  >__|   
         \/          \/           \/     \/             \/       \/     \/    \/              
```
# Internallinker

Automatically generate internal links between your markdown files.

# Notice

This isn't alpha yet - it's plain broken.

# Philosophy

You should link internal pages of your website up for a better user experience and better SEO.

# What it does

* This will go through a folder of markdown posts in a folder.
* It'll create a list of all the keywords that each post relates to (based on their frontmatter).
* It then loops through all the blog post text for every post, and when a keyword is used, it suggests an internal link is made

# Todo

This doesn't work yet:

* this needs to create a useful output of the suggested links to be inserted from the json it creates. Ideally it'd literally edit the files directly. You could then use a pull request to check out the diff to remove links that don't make sense. 
  * this is midway implemented in `generate-links.py`
* perhaps add a frontend?

## Pre-requisites

### installed stuff

First, make sure you have some markdown blog posts in the /blog folder.
These must have YAML front matter, that contains keywords
Keywords should be split by commas (without spaces)

Now you need to install one library:

Install pyyaml:

```
pip3 install virtualenv
virtualenv --python=python3 venv
source venv/bin/activate
pip install pyyaml
```
## To use

- run `python generate-keywords.py`
- run `python generate-links.py`

## How it works

- `generate-keywords.py` runs through every post in the blog folder
- it then looks for keywords listed in the YAML (the top bit above the content)
- it puts these into a big json (`keywordAssociations.json`)
- `generate-links.py` then runs through every blog post, finds keyword matches and inserts a link