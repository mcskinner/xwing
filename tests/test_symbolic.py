from xwing import X


def test_basics():
    x2 = X * 2
    assert x2(3) == 6
