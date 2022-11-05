import pandas as pd

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


def test_df():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    expected = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [5, 7, 9]})

    actual = df.assign(c=X.a + X.b)
    pd.testing.assert_frame_equal(actual, expected)


def test_df_nullable():
    df = pd.DataFrame({"nullable": [1, 2, None]})
    expected = pd.DataFrame({"nullable": [1, 2, None], "isnull": [False, False, True]})

    actual = df.assign(isnull=X._.isnull())
    pd.testing.assert_frame_equal(actual, expected)
