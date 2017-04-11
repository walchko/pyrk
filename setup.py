from setuptools import setup
from pyxl320 import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution


PACKAGE_NAME = 'pyrk'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	description="A simple runge-kutta 4 integrator",
	long_description=open('README.rst').read(),
	author="Kevin Walchko",
	author_email='kevin.walchko@outlook.com',
	license="MIT",
	url="http://github.com/walchko/{}".format(PACKAGE_NAME),
	packages=[PACKAGE_NAME],
	keywords='ode integration rk4 rk runge kutta',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: Scientific/Engineering',
		'Topic :: Software Development'
	],
	# setup_requires=[
	# 	# 'nose',
	# 	# 'coverage',
	# 	# 'mock'
	# ],
	cmdclass={
		'make': BuildCommand,
		'publish': PublishCommand
	},
)
