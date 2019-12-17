#!/usr/bin/env python3
# -*-coding:utf-8 -*

from setuptools import setup, find_packages

with open("README.md", "r") as longdesc:
      long_description = longdesc.read()

setup(name='ai42',
      version='1.0.0',
      description='An example of how to build a package',
      long_description=long_description,
      url='http://github.com/quarkgluant/boot-camp-python/tree/master/day02/ex04',
      author='Quarkgluant',
      author_email='pathibul.r@gmail.com',
      license='MIT',
      packages=find_packages(where='ai42'),
      package_dir={'': 'ai42'},
      zip_safe=False),