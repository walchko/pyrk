Runge-Kutta 4
==============

.. image:: https://travis-ci.org/walchko/pyrk.svg?branch=master
	:target: https://travis-ci.org/walchko/pyrk

A simple implementation of `Runge-Kutta <https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods>`_
for python.

Setup
--------

Install
~~~~~~~~~

::

	pip install pyrk


Develop
~~~~~~~~~~

::

	git clone https://github.com/walchko/pyrk
	cd pyrk
	pip install -e .

Usage
--------

See the examples in the `docs <https://github.com/walchko/pyrk/blob/master/doc/runge-kutta.ipynb>`_ folder or a simple one:

.. code:: python

	from __future__ import division, print_function
	from pyrk import RK4
	import numpy as np
	import matplotlib.pyplot as plt

	def vanderpol(t, xi, u):
		dx, x = xi
		mu = 4.0 # damping

		ddx = mu*(1-x**2)*dx-x
		dx = dx

		return np.array([ddx, dx])

	rk = RK4(vanderpol)
	t, y = rk.solve(np.array([0, 1]), .01, 200)

	y1 = []
	y2 = []
	for v in y:
		y1.append(v[0])
		y2.append(v[1])

	plt.plot(y1, y2)
	plt.ylabel('velocity')
	plt.xlabel('position')
	plt.grid(True)
	plt.show()
