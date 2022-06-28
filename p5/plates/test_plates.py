from plates import is_valid


def test_two_char_check():
    assert is_valid(
        "5555") == False, "first two characters should be alphabetic"


def test_length_check_lower():
    assert is_valid("h") == False, "length should be in between 2-6"


def test_length_check_higher():
    assert is_valid("hfgg5555") == False, "length should be in between 2-6"


def test_middle_no_check():
    assert is_valid("DH4HDD") == False, "can't contain letters after digit(s)"


def test_first_no_zero_check():
    assert is_valid("FG0") == False, "first no can't be zero"


def test_punc_check():
    assert is_valid("Fg^&") == False, "can't contain punctuation"


def test_all_valid():
    assert is_valid("hg7") == True
    assert is_valid("HG") == True
    assert is_valid("HG850") == True
    assert is_valid("HGhkh8") == True
    assert is_valid("ghrkf") == True
