import os
import sys
from setuptools import setup
from setuptools import find_packages

version = '0.5.2'

if sys.argv[-1] == 'publish':
	os.system("rm -fr dist")
	os.system("python setup.py sdist")
	os.system("twine upload dist/*")
	sys.exit()

if sys.argv[-1] == 'tag':
	os.system("git tag -a %s -m 'version %s'" % (version, version))
	os.system("git push --tags")
	sys.exit()

setup(
	name='pyrk',
	version=version,
	description="A simple runge-kutta 4 integrator",
	long_description=open('README.rst').read(),
	author="Kevin Walchko",
	author_email='kevin.walchko@outlook.com',
	# platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
	license="MIT",
	url="http://github.com/walchko/pyrk",
	# zip_safe=False,
	# packages=find_packages(exclude=['examples', 'test', 'doc']),  # doesn't work
	packages=find_packages(exclude=['examples', 'doc', 'tests']),
	# package_dir={'': 'pyrk'},
	# packages=['pyrk'],
	# install_requires=['nose'],
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
	],
	# test_suite='nose.collector',
	# test_suite='tests',
	# tests_require=['nose']
)
