##############################################
# The MIT License (MIT)
# Copyright (c) 2015 Kevin Walchko
# see LICENSE for full details
##############################################
from dataclasses import dataclass
from dataclasses import field
from typing import Callable
import numpy as np

@dataclass()
class RK4:
    """
    Implements a Runge-Kutta 4 as explained here:
    https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

    f - function(t, y, u)
    where:
        t - time
        y - state
        u - control force or other parameters for function
    """

    func: Callable[[float,np.ndarray, np.ndarray,float], np.ndarray]
    dt: float = field(default=0.0)

    def solve(self, y, h, t_end):
        """
        Given a function, initial conditions, step size and end value, this will
        calculate an unforced system. The default start time is t=0.0, but this
        can be changed.

        y - initial state
        h - step size
        n - stop time
        """
        ts = []
        ys = []
        yi = y
        ti = 0.0
        while ti < t_end:
            ts.append(ti)
            yi = self.__step(ti, yi, None, h)
            ys.append(yi)
            ti += h
        return ts, ys

    def __step(self, t, y, u, h):
        """
        This is called by solve, but can be called by the user who wants to
        run through an integration with a control force.

        y - state at t
        u - control inputs at t
        t - time
        h - step size
        """
        k1 = h * self.func(t, y, u)
        k2 = h * self.func(t + .5*h, y + .5*h*k1, u)
        k3 = h * self.func(t + .5*h, y + .5*h*k2, u)
        k4 = h * self.func(t + h, y + h*k3, u)
        return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    def __call__(self, t, y, u, h=None):
        """Alternative to calling step()"""
        if h is None:
            h = self.dt
        return self.__step(t, y, u, h)
