
.. image:: https://github.com/walchko/pyrk/raw/master/pics/math2.jpg
	:alt: Header pic

Runge-Kutta 4
==============

.. image:: https://travis-ci.org/walchko/pyrk.svg?branch=master
	:target: https://travis-ci.org/walchko/pyrk
	:alt: Travis-ci
.. image:: https://landscape.io/github/walchko/pyrk/master/landscape.svg?style=flat
   :target: https://landscape.io/github/walchko/pyrk/master
   :alt: Code Health
.. image:: https://img.shields.io/pypi/pyversions/pyrk.svg
	:target:  https://pypi.python.org/pypi/pyrk/
	:alt: Python Versions
.. image:: https://img.shields.io/pypi/v/pyrk.svg
    :target: https://pypi.python.org/pypi/pyrk/
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/l/pyrk.svg
    :target: https://pypi.python.org/pypi/pyrk/
    :alt: License


A simple implementation of `Runge-Kutta <https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods>`_
for python. This supports both python 2 and python 3.

Setup
--------

Install
~~~~~~~~~

The preferred method of installation is using ``pip``::

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

MIT License
----------------

Copyright (c) 2015 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
