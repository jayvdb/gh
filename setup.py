#!/usr/bin/env python
"""
gh
==========
.. code:: shell
  $ gh user
  $ gh repos/dvershinin/lastverion/license
"""

from setuptools import find_packages, setup
import os

install_requires = ["requests", "packaging", "cachecontrol", "lockfile", "appdirs"]
tests_requires = ["pytest>=4.4.0", "flake8", "pytest-xdist"]

with open("README.md", "r") as fh:
    long_description = fh.read()

base_dir = os.path.dirname(__file__)

version = {}
with open(os.path.join(base_dir, "gh", "__about__.py")) as fp:
    exec(fp.read(), version)

setup(
    name="gh-api",
    version=version["__version__"],
    author="Danila Vershinin",
    author_email="info@getpagespeed.com",
    url="https://github.com/dvershinin/gh",
    description="Low-level GitHub API request interface. With caching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    license="BSD",
    install_requires=install_requires,
    extras_require={
        "tests": install_requires + tests_requires,
    },
    tests_require=tests_requires,
    include_package_data=True,
    entry_points={"console_scripts": ["gh = gh:main"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
