#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'urllib3==1.22',
    'attrs==18.1.0',
    'certifi==2018.4.16',
    'chardet==3.0.4',
    'click==6.7',
    'idna==2.6',
    'jsonschema==2.6.0',
    'more-itertools==4.1.0',
    'py==1.5.3',
    'pytz==2018.3',
    'PyYAML==3.12',
    'raven==6.8.0',
    'requests==2.18.4',
    'shortuuid==0.5.0',
    'six==1.11.0',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'urllib3==1.22',
    'attrs==18.1.0',
    'certifi==2018.4.16',
    'chardet==3.0.4',
    'click==6.7',
    'idna==2.6',
    'jsonschema==2.6.0',
    'more-itertools==4.1.0',
    'pluggy==0.6.0',
    'py==1.5.3',
    'pytest==3.5.1',
    'pytz==2018.3',
    'PyYAML==3.12',
    'raven==6.8.0',
    'requests==2.18.4',
    'shortuuid==0.5.0',
    'six==1.11.0',
]

setup(
    name='pyclean',
    version='0.1.0',
    description="clean practices",
    long_description=readme + '\n\n' + history,
    author="Carlos Ramirez",
    author_email='carlos.ramirez@bahnlink.com',
    url='https://github.com/bahnlink/black',
    packages=find_packages(include=['clean.*', 'clean.exceptions']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='clean architecture',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)