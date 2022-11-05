from xwing import X


def test_basics():
    x2 = X * 2
    assert x2(3) == 6


def test_wing():
    class Obj:
        def plus1(self, x):
            return x + 1

    obj = Obj()
    assert X._.plus1(3)(obj) == 4
