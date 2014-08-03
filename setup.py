#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'thoth==0.0.1',
]

setup(
    name='thothslack',
    version='0.0.1',
    description='chat bot service for thoth',
    author='xica development team',
    author_email='info@xica.net',
    url='http://xica-inc.com',
    packages=find_packages(),
    install_requires=install_requires,
)
