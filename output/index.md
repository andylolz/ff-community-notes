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
        <th>Tweet language</th>
        <th>Deleted?</th>
        <th>Username</th>
        <th>Tweet content</th>
      </tr>
    </thead>
    <tbody>
    </tbody>
  </table>
</div>

<script>
  let table = new DataTable('table', {
    layout: {
      top2Start: 'search',
      top: 'searchPanes',
      topStart: 'info',
      topEnd: 'paging',
      bottomStart: 'info',
      bottom2Start: 'pageLength'
    },
    fixedHeader: true,
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
        },
        searchable: false,
        searchPanes: {
          show: false
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
        },
        searchable: false,
        searchPanes: {
          show: false
        }
      },
      {
        data: 'tweet_id', width: '550px', render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          content = row['tweet'] ? row['tweet'] : '';
          return '<blockquote class="twitter-tweet">' + content + '<a href="https://twitter.com/_/status/' + data + '"></a></blockquote>';
        },
        searchPanes: {
          show: false
        }
      },
      {
        data: 'summary'
      },
      {
        data: 'reasons',
        searchPanes: {
          show: false
        }
      },
      {
        data: 'lang',
        visible: false,
        defaultContent: '',
        searchPanes: {
          emptyMessage: 'Unknown (deleted tweet)'
        }
      },
      {
        data: 'deleted',
        visible: false,
        defaultContent: 0,
        searchPanes: {
          show: true
        }
      },
      {
        data: 'user',
        searchable: true,
        visible: false,
        defaultContent: '',
        searchPanes: {
          show: false
        }
      },
      {
        data: 'tweet',
        searchable: true,
        visible: false,
        defaultContent: '',
        searchPanes: {
          show: false
        }
      },
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    },
    searchPanes: {
      orderable: false,
      preSelect: [
        {
          column: 5,
          rows: ['en', 'zxx']
        },
        {
          column: 6,
          rows: [0]
        },
      ],
      initCollapsed: true
    }
  });

  twttr.events.bind(
    'rendered',
    function () {
      table.fixedHeader.adjust();
    }
  );
</script>
