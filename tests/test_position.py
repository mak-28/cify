import numpy as np

from cify.position import Position
from cify.objective_function import ObjectiveFunction


def test_init_with_vector():
    vector = np.random.random(10)
    position = Position(vector)
    assert np.array_equal(position.vector, vector)
    position = Position(vector.tolist())
    assert np.array_equal(position.vector, vector)


def test_init_with_objective_function():
    f = ObjectiveFunction(lambda x: sum(x**2), bounds=[[0, 1]] * 10)
    position = Position(f)
    assert position.vector is not None


def test_eval_on_init():
    f = ObjectiveFunction(lambda x: 0.0, bounds=[[0, 1]] * 10)
    Position(f, eval_on_init=False)
    assert f.evaluations == 0
    Position(f, eval_on_init=True)
    assert f.evaluations == 1


if __name__ == "__main__":
    test_init_with_vector()
    test_init_with_objective_function()
    test_eval_on_init()
