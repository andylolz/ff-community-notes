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
    fixedHeader: true,
    ajax: {
      url: '{{ '/data/notes.json' | relative_url }}',
      "dataSrc": function ( data ) {
        return data.filter(function(item) {
          if (item.deleted === 1) {
            return false;
          }
          return (item.lang === undefined || ['en', 'zxx'].includes(item.lang));
        });
      }
    },
    columns: [
      {
        data: 'created_at', render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          return '<a href="https://twitter.com/i/birdwatch/t/' + row['tweet_id'] + '" target="_blank">' + luxon.DateTime.fromISO(data).toFormat('d MMM yyyy') + '</a>';
        },
        searchable: false
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
        },
        searchable: false
      },
      {
        data: 'tweet_id', width: '550px', render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          content = row['tweet'] ? row['tweet'] : '';
          return '<blockquote class="twitter-tweet">' + content + '<a href="https://twitter.com/_/status/' + data + '"></a></blockquote>';
        },
        searchable: false
      },
      {
        data: 'summary',
      },
      {
        data: 'reasons'
      },
      {
        data: 'user',
        searchable: true,
        visible: false,
        defaultContent: ''
      },
      {
        data: 'tweet',
        searchable: true,
        visible: false,
        defaultContent: ''
      }
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    }
  });

  twttr.events.bind(
    'rendered',
    function () {
      table.fixedHeader.adjust();
    }
  );
</script>
