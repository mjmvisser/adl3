#!/usr/bin/env python

from distutils.core import setup

files = ["atitweak", "adl3/*"]

setup(name="adl3",
      version="0.6",
      description="ADL (AMD Display Library)",
      author="Mark Visser",
      author_email="mjmvisser@gmail.com",
      url="https://github.com/mjmvisser/adl3",
      packages=["adl3"],
      scripts=["atitweak"],
      zip_safe=True,
      classifiers = [
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: Public Domain",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.6",
          "Topic :: Multimedia :: Video",
          "Topic :: Multimedia :: Graphics"]
      )
