#!/usr/bin/env python

from setuptools import setup, find_packages

REQUIRES = [
      'pydrive',
      'oauth2client',
      'google',
]

setup(name='colab_util',
      version='0.0.2',
      description='Colab file system utilities',
      author='Yuanruo',
      author_email='liangyuanruo@gmail.com',
      packages=find_packages(),
      license='LICENSE',
      install_requires=REQUIRES
      )
