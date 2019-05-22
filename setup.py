#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Franck Nijhof",
    author_email="opensource@frenck.dev",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Frenck's Python test package repository.",
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords=["frenck", "test"],
    name="frenck",
    packages=find_packages(include=["frenck"]),
    url="https://github.com/frenck/python-test",
    version="0.1.0",
    zip_safe=False,
    test_suite="tests",
)
