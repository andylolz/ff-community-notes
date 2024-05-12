---
title: How it works
---

Community note data is fetched regularly [from Twitter](https://twitter.com/i/communitynotes/download-data).

This data is always a couple of days old (**most recent data is from <time class="dt" datetime="{{ site.data.meta.most_recent }}" title="{{ site.data.meta.most_recent | date_to_rfc822 }}">{{ site.data.meta.most_recent }}</time>, scraped <time class="dt" datetime="{{ site.data.meta.scraped_at }}" title="{{ site.data.meta.scraped_at | date_to_rfc822 }}">{{ site.data.meta.scraped_at }}</time>**).

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’

We also attempt to filter out notes for deleted tweets and non-English tweets.

<script>
  const dts = document.getElementsByClassName('dt');
  for (var i = 0; i < dts.length; i++) {
    var dt = dts[i];
    dt.textContent = luxon.DateTime.fromISO(dt.textContent).toRelative();
  }
</script>
