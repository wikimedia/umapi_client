#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

__version__ = '0.1.1-dev'

setup(
    name='wmf_umapi_client',
    version=__version__,
    long_description=long_description,
    description='Client wrapper for Wikimedia UMAPI.',
    url='http://www.github.com/rfaulkner/umapi_client',
    author="Wikimedia Foundation",
    author_email="e3-team@lists.wikimedia.org",
    packages=['umapi_client',
	      ],
    package_data={
        'user_metrics.api': [
            'template/*',
        ],
        },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    data_files=[('.', ['README.md']),]
)
