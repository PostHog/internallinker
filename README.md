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

# What it does

* This will go through a folder of markdown posts in a folder.
* It'll create a list of all the keywords that each post relates to (based on their frontmatter).
* It then loops through all the blog post text for every post, and when a keyword is used, it suggests an internal link is made

# Todo

This doesn't work yet:

* keywordAssociations has wrong structure - it needs to work at a "link" level
* random example crap in keywordAssociations needs to be deleted
* this needs to create a useful output of the suggested links to be inserted. Ideally it'd literally edit the files directly. You could then use a pull request to check out the diff to remove links that don't make sense.


## Pre-requisites

Install pyyaml:

```
pip3 install virtualenv
virtualenv --python=python3 venv
source venv/bin/activate
pip install pyyaml
```

