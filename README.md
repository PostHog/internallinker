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

This is in Alpha. Please manually check the changes to your markdown before uploading!

# Philosophy

You should link internal pages of your website up for a better user experience and better SEO.

# What it does

* The user uploads one or more markdown posts (which must have keywords entered in the frontmatter) - see `example-posts` for the right format.
* It'll create a list of all the keywords that each post relates to (based on their frontmatter).
* It then loops through all the blog post text for every post, and when a keyword is used, it suggests an internal link is made
* the user can then grab the updated posts in the `generated-posts` folder

## Pre-requisites

First, make sure you have some markdown blog posts with keywords in their front matter (see `/example-posts` for the right format).

Second, install any needed dependencies.

```
pip3 install -r requirements.txt
virtualenv --python=python3 venv
source venv/bin/activate
```

Third, run flask with `flask run`

Fourth, now visit `http://127.0.0.1:5000/` in your browser

Fifth, if you wanto match on just `keywords` from your frontmatter, leave the topics checkbox empty. If you want to match on `keywords` _and_ `topics` then check the checkbox.

## How it works

- this is an app powered by Flask
- the user uploads one or more markdown posts
- in `app.py`, the function `generate_keywords()` runs through every uploaded post
- it then looks for keywords listed in the YAML (the top bit above the content)
- it puts these into a big json (`generated-posts/keywordAssociations.json`)
- in `app.py`, it then runs through every post, finds keyword matches and inserts a link
- there is fancy filtering - it won't insert a link inside another link, it won't link pages to themselves, and it won't insert a link that isn't an entire word (ie  it won't do this: [dog](https://en.wikipedia.org/wiki/Dog)s)
- the user can then get these updated posts in the folder `/generated-posts`
