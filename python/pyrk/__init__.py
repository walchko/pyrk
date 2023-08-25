##############################################
# The MIT License (MIT)
# Copyright (c) 2015 Kevin Walchko
# see LICENSE for full details
##############################################
from .pyrk import RK4


from importlib.metadata import version # type: ignore

__license__ = 'MIT'
__copyright__ = 'copyright (c) 2015 Kevin J. Walchko'
__author__ = 'Kevin J. Walchko'
__version__ = version("pyrk")
