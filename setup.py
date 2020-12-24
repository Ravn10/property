# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in property/__init__.py

setup(
	name='property',
	version=1.0,
	description='Property Management',
	author='Opensource Solutions Philippines',
	author_email='info@ossph.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
