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

This is in Alpha. It's not tested yet properly.

# Philosophy

You should link internal pages of your website up for a better user experience and better SEO.

# What it does

* This will go through a folder of markdown posts in a folder.
* It'll create a list of all the keywords that each post relates to (based on their frontmatter).
* It then loops through all the blog post text for every post, and when a keyword is used, it suggests an internal link is made

# Todo

* it feels messy running two scripts - combine them
* add a frontend
  * choose folder
  * produce table of files (with links) that it has loaded, and highlight which it has modified
* handle duplicated keywords
  * pick randomly between them *and* show user if this is the case

## Pre-requisites

### installed stuff

First, make sure you have some markdown blog posts in the /blog folder.
These must have YAML front matter, that contains keywords
Keywords should be split by commas (without spaces)

Second, install any needed dependencies.

```
pip3 install -r requirements.txt
virtualenv --python=python3 venv
source venv/bin/activate
```

## To use

- in both `generate-keywords.py` and `generate-links.py`, set `path` as the local path to the folder that contains the posts you want to modify
- run `python generate-keywords.py`
- run `python generate-links.py`

## How it works

- `generate-keywords.py` runs through every post in the blog folder
- it then looks for keywords listed in the YAML (the top bit above the content)
- it puts these into a big json (`keywordAssociations.json`)
- `generate-links.py` then runs through every blog post, finds keyword matches and inserts a link