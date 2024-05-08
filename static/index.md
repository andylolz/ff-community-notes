---
title: Twitter community notes
---

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…]({{ '/about/' | relative_url }})_

<div class="table-responsive">
  <table class="table table-striped" data-order='[[ 0, "desc" ]]'>
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
    </tbody>
  </table>
</div>

<script>
  let table = new DataTable('table', {
    ajax: {
      url: '{{ '/data/notes.json' | relative_url }}',
      dataSrc: ''
    },
    columns: [
        {
          data: 'created_at', render: function (data, type, row, meta) {
            if (type !== 'display') {
              return data;
            }
            return '<a href="https://twitter.com/i/birdwatch/t/' + row['tweet_id'] + '" target="_blank">' + luxon.DateTime.fromISO(data).toFormat('d MMM yyyy') + '</a>';
          }
        },
        {
          data: 'shown', defaultContent: '', render: function (data, type, row, meta) {
            if (data === undefined) {
              return '';
            }
            if (type !== 'display') {
              return data;
            }
            content = luxon.DateTime.fromISO(data).toFormat('d MMM yyyy')
            if (row['removed']) {
              content += ' (since removed)';
            }
            return content;
          }
        },
        {
          data: 'tweet_id', width: '550px', render: function (data, type, row, meta) {
            if (type !== 'display') {
              return data;
            }
            return '<blockquote class="twitter-tweet"><a href="https://twitter.com/_/status/' + data + '"></a></blockquote>';
          }
        },
        {
          data: 'summary',
        },
        {
          data: 'reasons'
        }
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    }
  });
</script>
