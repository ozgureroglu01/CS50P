from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_start_with_h_not_hello():
    assert value("How you doing?") == 20
    assert value("how you doing?") == 20

def test_other():
    assert value("What's happening?") == 100
    assert value("what's happening?") == 100

