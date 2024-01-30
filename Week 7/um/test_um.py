from um import count

def test_count_alone():
    assert count("um") == 1
    assert count("um um um") == 3

def test_count_with_symbols():
    assert count("um?") == 1
    assert count("?um?") == 1
    assert count(".um um!") == 2

def test_count_in_sentences():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

