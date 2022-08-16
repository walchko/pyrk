from pyrk import RK4
from math import pi
from math import cos


def test_solve():
    rk = RK4(lambda t, y, u: cos(t))
    y = 0.0
    t, y = rk.solve(y, 0.01, 2.0*pi)
    assert(y[-1] < 0.01)


def test_step():
    rk = RK4(lambda t, y, u: cos(t))
    y = 0.0
    t = 0.0
    step = 0.01

    while t <= 2.0*pi:
        y = rk(t, y, None, step)
        t += step

    assert(y < 0.01)
