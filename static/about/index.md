---
title: How it works
---

Community note data is fetched regularly from [https://twitter.com/i/communitynotes/download-data](https://twitter.com/i/communitynotes/download-data). This data is always a couple of days old (last updated: <span class="timestamp">{{ site.data.notes | map: "created_at" | sort | last | date_to_rfc822 }}</span>).

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’