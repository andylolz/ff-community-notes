# Twitter community notes

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…](#how-it-works)_

https://andylolz.github.io/x-community-notes/

## How it works

Community note data is fetched regularly [from Twitter](https://twitter.com/i/communitynotes/download-data).

This data is always a couple of days old.

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’

## Running locally

Initial setup:

```shell
# Install python dependencies
pip install -r requirements_dev.txt

# Install ruby dependencies (Jekyll)
bundle install
```

Then to run:

```shell
# Fetch notes
python -m x_notes

# Start the development server
cd static
jekyll serve --baseurl ""
```
