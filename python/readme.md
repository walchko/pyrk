![Header pic](https://github.com/walchko/pyrk/raw/master/pics/math2.jpg)

# Runge-Kutta

[![Actions Status](https://github.com/walchko/pyrk/workflows/pytest/badge.svg)](https://github.com/walchko/pyrk/actions)
![PyPI - License](https://img.shields.io/pypi/l/pyrk.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrk.svg)
![PyPI - Format](https://img.shields.io/pypi/format/pyrk.svg)
![PyPI](https://img.shields.io/pypi/v/pyrk.svg)

A simple implementation of
[Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)
for python.

## Usage

Integrates a function x_dot = f(time, x, u). See the examples in the
[docs](https://github.com/walchko/pyrk/blob/master/doc/runge-kutta.ipynb)
folder or a simple one:

``` python
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
```

## Alternative

If you want to use `scipy` (which is good, but big), you can do:

```python
from scipy.integrate import solve_ivp as rk45

def func(t,x,u):
    # cool differential equations
    # ...
    return x

t = 0
dt = 0.01
y = np.array([0,0,0]) # initial state

for _ in tqdm(range(steps)):
    u = np.array([1,2,3]) # some inputs to func (i.e., control effort)

    y = rk45(func, [t, t+step], y, args=(u,))

    if y.success == False:
        print("Oops")

    y = y.y[:,-1]

    # probably save t, u and y into arrays for plotting
    t += step
```

# MIT License

**Copyright (c) 2015 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
