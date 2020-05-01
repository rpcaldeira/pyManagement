# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyManagement',
    version='0.0.1',
    description='Python-based operating system management service',
    long_description=readme,
    author='Rui Pedro Caldeira',
    author_email='pymanagement@rpcnet.net',
    url='https://github.com/rpcaldeira/pyManagement',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)