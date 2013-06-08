#!/usr/bin/env python

from setuptools import setup

version = 0.1

setup(
    name="arc",
    version=version,
    author="Matthew Jaffee",
    author_email="matthew.jaffee@gmail.com",
    py_modules=['arc'],
    install_requires = [
        "docopt"
    ],
    entry_points = {
        'console_scripts': [
            'arc = arc:main'
        ]
    }
)
