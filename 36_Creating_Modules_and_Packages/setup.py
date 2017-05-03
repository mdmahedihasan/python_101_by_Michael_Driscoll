#!/usr/bin/env python

from setuptools import setup
from distutils.core import setup


setup(
    name="mymath",
    version="0.1",
    description="a silly math package",
    author="Mahedi",
    author_email="mahedi_h@yahoo.com",
    url="http://www.mymath.org/",
    packages=["mymath", "mymath.adv"]
)