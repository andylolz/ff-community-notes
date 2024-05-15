import pytest

from x_notes import notes


@pytest.mark.parametrize("test_input,expected", [
    ("a http://example.com b", 'a <a target="_blank" href="http://example.com">http://example.com</a> b'),
    ("https://example.com/", '<a target="_blank" href="https://example.com/">https://example.com/</a>'),
    ("http://example.com/a/long/path?ex=ample#com", '<a target="_blank" href="http://example.com/a/long/path?ex=ample#com">http://example.com/a/long/path?ex…</a>'),
])
def test_urlize(test_input, expected):
    assert notes.urlize(test_input) == expected
