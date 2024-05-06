---
title: Twitter community notes
---

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…]({{ '/about/' | relative_url }})_

<div class="table-responsive">
  <table class="table table-striped" data-order='[[ 1, "desc" ]]'>
    {% assign sorted_rows = site.data.notes | sort:'created_at' | reverse %}
    {% for row in sorted_rows %}

    {% if forloop.first %}
    <thead>
      <tr>
        <th class="d-none">Tweet ID</th>
        <th>Note created</th>
        <th>Note shown</th>
        <th class="d-none">Note removed</th>
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
        <td class="d-none">{{ row['tweet_id'] }}</td>
        <td>{{ row['created_at'] }}</td>
        {% if status %}
        <td>{{ status.from }}</td>
        {% else %}
        <td></td>
        {% endif %}
        {% if status and status.to %}
        <td class="d-none">{{ status.to }}</td>
        {% else %}
        <td class="d-none"></td>
        {% endif %}
        <td><blockquote class="twitter-tweet"><a href="https://twitter.com/_/status/{{ row['tweet_id'] }}"></a></blockquote></td>
        <td>{{ row['summary'] }}</td>
        <td>{{ row['reasons'] }}</td>
      </tr>
    {% endfor %}

    </tbody>
  </table>
</div>

<script>
  let table = new DataTable('table', {
    columnDefs: [
      {
        target: 1,
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          return '<a href="https://twitter.com/i/birdwatch/t/' + row[0] + '" target="_blank">' + luxon.DateTime.fromISO(data).toFormat('d MMM yyyy') + '</a>';
        }
      },
      {
        target: 2,
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          if (data === '') {
            return data;
          }
          data = luxon.DateTime.fromISO(data).toFormat('d MMM yyyy');
          if (row[3] !== '') {
            data = data + ' (since removed)';
          }
          return data;
        }
      },
      {
        targets: [0, 3],
        visible: false
      }
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    }
  });
</script>
