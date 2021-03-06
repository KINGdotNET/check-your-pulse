"""
This is the setup module for the example project.

Based on:

- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
"""

# Standard Python Libraries
from glob import glob
from os.path import basename, splitext

# Third-Party Libraries
from setuptools import setup

# Author details
author = ("Cyber and Infrastructure Security Agency",)
author_email = "threathunting@cisa.dhs.gov"


def readme():
    """Read in and return the contents of the project's README.md file."""
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def package_vars(version_file):
    """Read in and return the variables defined by the version_file."""
    pkg_vars = {}
    with open(version_file) as f:
        exec(f.read(), pkg_vars)  # nosec
    return pkg_vars


setup(
    name="pulse-check-logs-tools",
    # Versions should comply with PEP440
    version="1.0.0",
    description="Check logs for attempts at CVE-2019-11510",
    long_description=readme(),
    long_description_content_type="text/markdown",
    # HIRT "homepage"
    url="https://www.cisa.gov/cyber-incident-response",
    # The project's main homepage
    download_url="https://github.com/cisagov/check-your-pulse",
    # Author details
    author=author,
    author_email=author_email,
    license="License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Production/Stable",
        # Indicate who your project is intended for
        "Intended Audience :: System Administrators",
        # Pick your license as you wish (should match "license" above)
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # What does your project relate to?
    keywords="skeleton",
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.6",
)
