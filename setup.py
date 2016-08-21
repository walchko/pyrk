# import os
from setuptools import setup
from setuptools import find_packages

setup(
	name='pyrk',
	version='0.5.1',
	description="A simple runge-kutta 4 integrator",
	long_description=open('README.rst').read(),
	author="Kevin Walchko",
	author_email='kevin.walchko@outlook.com',
	# platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
	license="MIT",
	url="http://github.com/walchko/pyrk",
	# zip_safe=False,
	# packages=find_packages(exclude=['examples', 'test', 'doc']),  # doesn't work
	packages=find_packages('pyrk'),
	package_dir={'':'pyrk'},
	# packages=['pyrk'],
	keywords='ode integration rk4 rk runge kutta',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: Scientific/Engineering',
		'Topic :: Software Development'
	]
)
