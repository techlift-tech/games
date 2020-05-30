# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in games/__init__.py
from games import __version__ as version

setup(
	name='games',
	version=version,
	description='Games',
	author='Techlift',
	author_email='palash@techlift.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
