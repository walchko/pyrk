##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
import attr

@attr.s(slots=True)
class RK4:
    """
    Implements a Runge-Kutta 4 as explained here:
    https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

    f - function(t, y, u)
    where:
        t - time
        y - state
        u - control force
    """

    # def __init__(self, f):
    #     """
    #     Constructor which takes a function for integration.
    #
    #     f - function(t, y, u)
    #         where:
    #             t - time
    #             y - state
    #             u - control force
    #     """
    #     self.func = f

    func = attr.ib()

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
            yi = self.step(yi, None, ti, h)
            ys.append(yi)
            ti += h
        return ts, ys

    def step(self, y, u, t, h):
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

    def __call__(self, y, u, t, h):
        """Alternative to calling step()"""
        return self.step(y, u, t, h)
