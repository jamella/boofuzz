#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='boofuzz',
    download_url='https://github.com/jtpereyda/boofuzz',
    license='GPL',
    packages=['requests', 'boofuzz', 'boofuzz.legos', 'boofuzz.pgraph', 'boofuzz.utils',
              'unit_tests', 'utils', 'web'],
    package_dir={'requests': './requests',
                 'boofuzz': './boofuzz',
                 'boofuzz.legos': './boofuzz/legos',
                 'boofuzz.pgraph': './boofuzz/pgraph',
                 'boofuzz.utils': './boofuzz/utils',
                 'unit_tests': './unit_tests',
                 'utils': './utils',
                 'web': './web'
                 },
    package_data={'web': ['templates/*', 'static/css/*']},
    install_requires=['pydot2==1.0.33', 'tornado==4.0.2', 'Flask==0.10.1', 'pcapy', 'impacket']
)
