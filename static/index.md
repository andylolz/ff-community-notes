---
title: Twitter community notes
---

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…](#how-it-works)_

<table class="table table-striped" data-order='[[ 0, "desc" ]]'>
  {% for row in site.data.notes %}
  {% if forloop.first %}
  <thead>
    <tr>
      <th>Note created</th>
      <th>Note shown</th>
      <th>Tweet</th>
      <th>Note</th>
      <th>Reasons</th>
    </tr>
  </thead>
  <tbody>
  {% endif %}

  {% assign status = site.data.statuses[row['note_id']] %}
    {% if status.status == "unhelpful" %}
      {% continue %}
    {% endif %}
    <tr id="{{ row['note_id'] }}">
      <td><a target="_blank" href="https://twitter.com/i/birdwatch/t/{{ row['tweet_id'] }}">{{ row['created_at'] | date:"%Y-%m-%d" }}</a></td>
      {% if status %}
      <td>{{ status.from | date:"%Y-%m-%d" }}{% if status.to %} (since removed){% endif %}</td>
      {% else %}
      <td></td>
      {% endif %}
      <td><blockquote class="twitter-tweet"><a href="https://twitter.com/_/status/{{ row['tweet_id'] }}"></a></blockquote></td>
      <td>{{ row['summary'] }}</td>
      <td>{{ row['reasons'] }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

---

## How it works

Community note data is fetched regularly from [https://twitter.com/i/communitynotes/download-data](https://twitter.com/i/communitynotes/download-data). This data is always a couple of days old.

Notes are excluded if they meet any of the following criteria:

* Created more than a week ago
* Classifying the post as ‘not misleading’ (i.e. in support of the post)
* Currently rated ‘unhelpful’
