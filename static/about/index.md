---
title: How it works
---

{% comment %}
# this is actually the time the site was generated, but (in CI at least) we
# scrape and then generate, so this is Good Enough
{% endcomment %}
{% assign scraped_at = 'now' %}

{% assign updated_at = site.data.notes | map: "created_at" | sort | last %}

Community note data is fetched regularly [from Twitter](https://twitter.com/i/communitynotes/download-data).

This data is always a couple of days old (**most recent data is from <time class="dt" datetime="{{ updated_at }}" title="{{ updated_at | date_to_rfc822 }}">{{ updated_at }}</time>, scraped <time class="dt" datetime="{{ scraped_at }}" title="{{ scraped_at | date_to_rfc822 }}">{{ scraped_at | date_to_xmlschema }}</time>**).

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’

<script>
  const dts = document.getElementsByClassName('dt');
  for (var i = 0; i < dts.length; i++) {
    var dt = dts[i];
    dt.textContent = luxon.DateTime.fromISO(dt.textContent).toRelative();
  }
</script>
