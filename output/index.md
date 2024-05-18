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
        <th>Tweet status</th>
        <th>Username</th>
        <th>Tweet content</th>
      </tr>
    </thead>
    <tbody>
    </tbody>
  </table>
</div>

<script>
  /*
  This might not be quite right.
  It’s mostly BCP-47, but with some idiosyncracies.
  E.g.:
    * Hebrew is `iw` instead of `he`
    * Indonesian is `in` instead of `id`
    * Haitian Creole is included (`ht`)
  */
  const langLookup = {'af': 'Afrikaans', 'am': 'Amharic', 'ar': 'Arabic', 'arn': 'Mapudungun', 'as': 'Assamese', 'az': 'Azerbaijani', 'ba': 'Bashkir', 'be': 'Belarusian', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bo': 'Tibetan', 'br': 'Breton', 'bs': 'Bosnian', 'ca': 'Catalan', 'co': 'Corsican', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'dsb': 'Lower Sorbian', 'dv': 'Divehi', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Persian', 'fi': 'Finnish', 'fil': 'Filipino', 'fo': 'Faroese', 'fr': 'French', 'fy': 'Frisian', 'ga': 'Irish', 'gd': 'Scottish Gaelic', 'gl': 'Galician', 'gsw': 'Swiss German', 'gu': 'Gujarati', 'ha': 'Hausa', 'hi': 'Hindi', 'hr': 'Croatian', 'hrv': 'Serbo-Croatian', 'hsb': 'Upper Sorbian', 'ht': 'Haitian Creole', 'hu': 'Hungarian', 'hy': 'Armenian', 'ig': 'Igbo', 'ii': 'Yi', 'in': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'iw': 'Hebrew', 'ja': 'Japanese', 'ka': 'Georgian', 'kk': 'Kazakh', 'kl': 'Greenlandic', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'kok': 'Konkani', 'kb': 'Kurdi', 'ky': 'Kyrgyz', 'lb': 'Luxembourgish', 'lo': 'Lao', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mi': 'Maori', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mn': 'Mongolian', 'moh': 'Mohawk', 'mr': 'Marathi', 'ms': 'Malay', 'mt': 'Maltese', 'my': 'Burmese', 'nb': 'Norwegian (Bokmål)', 'ne': 'Nepali', 'nl': 'Dutch', 'nn': 'Norwegian (Nynorsk)', 'no': 'Norwegian', 'oc': 'Occitan', 'or': 'Odia', 'pa': 'Punjabi', 'pl': 'Polish', 'prs': 'Dari', 'ps': 'Pashto', 'pt': 'Portuguese', 'quc': 'K\'iche', 'qu': 'Quechua', 'rm': 'Romansh', 'ro': 'Romanian', 'ru': 'Russian', 'rw': 'Kinyarwanda', 'sa': 'Sanskrit', 'sah': 'Yakut', 'se': 'Sami (Northern)', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'sma': 'Sami (Southern)', 'smj': 'Sami (Lule)', 'smn': 'Sami (Inari)', 'sms': 'Sami (Skolt)', 'sq': 'Albanian', 'sr': 'Serbian', 'st': 'Sesotho', 'sv': 'Swedish', 'sw': 'Kiswahili', 'syc': 'Syriac', 'ta': 'Tamil', 'te': 'Telugu', 'tg': 'Tajik', 'th': 'Thai', 'tk': 'Turkmen', 'tl': 'Tagalog', 'tn': 'Tswana', 'tr': 'Turkish', 'tt': 'Tatar', 'tzm': 'Tamazight', 'ug': 'Uyghur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'wo': 'Wolof', 'xh': 'Xhosa', 'yo': 'Yoruba', 'zh': 'Chinese', 'zu': 'Zulu', 'art': 'X', 'qam': 'X', 'qct': 'X', 'qht': 'X', 'qme': 'X', 'qst': 'X', 'und': 'X', 'zxx': 'X'}
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
        data: 'created_at',
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          return '<a href="https://twitter.com/i/birdwatch/t/' + row['tweet_id'] + '" target="_blank">' + luxon.DateTime.fromISO(data).toFormat('d MMM yyyy') + '</a>';
        },
        searchable: false
      },
      {
        data: 'shown',
        defaultContent: '',
        render: function (data, type, row, meta) {
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
        data: 'tweet_id',
        width: '550px',
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          content = row['tweet'] ? row['tweet'] : '';
          return '<blockquote class="twitter-tweet">' + content + '<a href="https://twitter.com/_/status/' + data + '"></a></blockquote>';
        }
      },
      {
        data: 'summary'
      },
      {
        data: 'reasons'
      },
      {
        data: 'lang',
        visible: false,
        defaultContent: '',
        render: function (data, type, row, meta) {
          if (!data) {
            return 'X unknown (deleted tweet)';
          }
          const niceName = langLookup[data];
          if (niceName === 'X') {
            // there are a handful of language codes that are used for
            // esoteric twitter things, including emoji-only tweets (`art`)
            // and hashtag-only tweets (`qht`). We lump these all together
            return 'X special';
          }
          return niceName + ' (' + data + ')';
        }
      },
      {
        data: 'deleted',
        visible: false,
        defaultContent: 0,
        render: function (data, type, row, meta) {
          if (type === 'display') {
            return (data === 1) ? 'Deleted' : 'Published';
          }
          return data;
        }
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
      },
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    },
    searchPanes: {
      orderable: false,
      columns: [5, 6],
      preSelect: [
        {
          column: 5,
          rows: ['English (en)', 'X special', 'X unknown (deleted tweet)']
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
