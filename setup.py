"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import os

from setuptools import setup, find_packages

# pylint: disable=redefined-builtin

here = os.path.abspath(os.path.dirname(__file__))  # pylint: disable=invalid-name

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()  # pylint: disable=invalid-name

setup(
    name='swagger_to',
    version='2.0.0',
    description='Generates code from swagger definitions; an alternative to swagger codegen',
    long_description=long_description,
    url='https://bitbucket.org/parqueryopen/swagger_to',
    author='Marko Ristin',
    author_email='marko@parquery.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='swagger code generation go typescript server client angular',
    python_requires='>=3.5',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pyyaml>=3.12'],
    extras_require={'dev': ['mypy==0.560', 'pylint==1.8.2', 'yapf==0.20.2']},
    py_modules=['swagger_to'],
    scripts=['bin/swagger_to_go_server.py', 'bin/swagger_to_py_client.py', 'bin/swagger_to_ts_angular5_client.py'])
