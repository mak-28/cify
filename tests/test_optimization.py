import numpy as np

from cify import Optimization


def test_cmp():
    a = np.random.uniform(0.0, 0.5)
    b = np.random.uniform(0.5, 1.0)
    opt = Optimization.Min
    assert opt.cmp(a, b) is True
    assert opt.cmp(b, a) is False
    assert opt.cmp(a, a) is False
    assert opt.cmp(a, a, equal=True) is True
    opt = Optimization.Max
    assert opt.cmp(a, b) is False
    assert opt.cmp(b, a) is True
    assert opt.cmp(a, a) is False
    assert opt.cmp(a, a, equal=True) is True


def test_verb():
    opt = Optimization.Min
    assert opt.verb() == "Minimizing"
    opt = Optimization.Max
    assert opt.verb() == "Maximizing"


if __name__ == "__main__":
    test_cmp()
    test_verb()
