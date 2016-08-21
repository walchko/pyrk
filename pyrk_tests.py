#!/usr/bin/env python

from __future__ import division
from pyrk import RK4
from math import sin, pi, cos
# import numpy as np
# import matplotlib.pyplot as plt


def test_solve():
	rk = RK4(lambda t, y, u: cos(t))
	y = 0.0
	t, y = rk.solve(y, 0.01, 2.0*pi)
	# print(y)
	# print(y[-1])
	# plt.plot(t, y)
	# plt.show()
	assert(y[-1] < 0.01)

def test_step():
	rk = RK4(lambda t, y, u: cos(t))
	y = 0.0
	t = 0.0
	step = 0.01

	while t <= 2.0*pi:
		y = rk.step(y, None, t, step)
		t += step

	# print(y)
	assert(y < 0.01)


# test_solve()
test_step()
