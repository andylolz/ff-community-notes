# Twitter community notes

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…](#how-it-works)_

https://andylolz.github.io/ff-community-notes/

## How it works

Community note data is fetched regularly from [https://twitter.com/i/communitynotes/download-data](https://twitter.com/i/communitynotes/download-data). This data is always a couple of days old.

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’

## Running locally

Initial setup:

```shell
# Copy files into place
cp -r static/* output

# Install python dependencies
pip install -r requirements_dev.txt

# Install ruby dependencies (Jekyll)
bundle install
```

Then to run:

```shell
# Fetch notes
python -m ff_notes.fetch_notes

# Fetch note statuses
python -m ff_notes.fetch_statuses

# Start the development server
cd output
jekyll serve --baseurl ""
```
