---
title: How it works
---

{% assign updated_at = site.data.notes | map: "created_at" | sort | last %}

Community note data is fetched regularly [from Twitter](https://twitter.com/i/communitynotes/download-data).

This data is always a couple of days old (**the most recent data is from <time id="updatedAt" datetime="{{ updated_at }}" title="{{ updated_at | date_to_rfc822 }}">{{ updated_at }}</time>**).

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’

<script>
  const dt = document.getElementById('updatedAt');
  const rel = luxon.DateTime.fromISO(dt.textContent).toRelative();
  dt.textContent = rel;
</script>
