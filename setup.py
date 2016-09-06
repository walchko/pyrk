#!/usr/bin/enb python

from __future__ import print_function
import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from pyrk import __version__ as VERSION


# http://fgimian.github.io/blog/2014/04/27/running-nose-tests-with-plugins-using-the-setuptools-test-command/
class NoseTestCommand(TestCommand):
	def run_tests(self):
		print('Running nose tests ...')
		os.system('nosetests -v tests/test_pyrk.py')


class PublishCommand(TestCommand):
	def run_tests(self):
		print('Publishing to PyPi ...')
		os.system("python setup.py sdist")
		os.system("twine upload dist/pyrk-{}.tar.gz".format(VERSION))


class GitTagCommand(TestCommand):
	def run_tests(self):
		print('Creating a tag for version {} on git ...'.format(VERSION))
		os.system("git tag -a {} -m 'version {}'".format(VERSION, VERSION))
		os.system("git push --tags")


class CleanCommand(TestCommand):
	def run_tests(self):
		print('Cleanning up ...')
		os.system('rm -fr pyrk.egg-info dist')

setup(
	name='pyrk',
	version=VERSION,
	description="A simple runge-kutta 4 integrator",
	long_description=open('README.rst').read(),
	author="Kevin Walchko",
	author_email='kevin.walchko@outlook.com',
	license="MIT",
	url="http://github.com/walchko/pyrk",
	packages=find_packages(exclude=['examples', 'doc', 'tests']),
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
	],
	setup_requires=[
		'nose',
		# 'coverage',
		# 'mock'
	],
	cmdclass={
		'test': NoseTestCommand,
		'publish': PublishCommand,
		'tag': GitTagCommand,
		'clean': CleanCommand
	},
)
