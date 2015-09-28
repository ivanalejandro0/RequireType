#!/usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
# history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
    'nose',
]

setup(
    name='RequireType',
    version='0.1.0',
    description='',
    # long_description=readme + '\n\n' + history,
    long_description=readme,
    author='Ivan Alejandro',
    author_email='ivanalejandro0@gmail.com',
    url='https://github.com/ivanalejandro0/RequireType',
    packages=[
        'requiretype',
    ],
    package_dir={'requiretype':
                 'requiretype'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='requiretype',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
