from twttr import shorten


def test_single_word():
    assert shorten("hEllo") == "hll", "should be 'hll'"
    assert shorten("Twitter") == "Twdttr", "should be 'Twttr'"


def test_multiple_words():
    assert shorten(
        "dAsun SatHsara BANdara") == "dsn StHsr BNdr", "should be 'dsn StHsr BNdr' "
