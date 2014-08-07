#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'djehuty==0.0.2',
]

setup(
    name='djehutyslack',
    version='0.0.2',
    description='chat bot service for djehuty',
    author='xica development team',
    author_email='info@xica.net',
    url='http://xica-inc.com',
    packages=find_packages(),
    install_requires=install_requires,
)
