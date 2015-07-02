#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = open("requirements.txt").read()

test_requirements = [
    # TODO: put package test requirements here
]

import version

setup(
    name='moviesidsdb-client',
    version=version.APP_VERSION,
    description="moviesidsdb python client",
    long_description=readme + '\n\n' + history,
    author="Jean-Christophe",
    author_email='jc.saaddupuy@fsfe.org',
    url='https://github.com/jcsaaddupuy/moviesidsdb-client',
    packages=[
        'moviesidsdb',
    ],
    package_dir={'moviesidsdb':
                 'moviesidsdb'},


    # configure the default command line entry point.
    entry_points={
        'console_scripts': [
            'moviesidsdb.client-cli = moviesidsdb.client.bin.cli:main',
        ]
    },



    include_package_data=True,
    install_requires=requirements,
    license="WTFPL",
    zip_safe=False,
    keywords='moviesidsdb client, movie identification',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
