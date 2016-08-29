# -*- coding: utf-8 -*-
"""Package implements a mailroom helper function."""
from setuptools import setup

setup(
    name='Code Katas',
    description='My Codewars solutions.',
    version='0.1.0',
    author='Justin Lange',
    author_email='well1912@gmail.com',

    package_dir={'': 'src'},
    py_modules=['sum_terms'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
