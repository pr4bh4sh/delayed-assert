from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='delayed_assert',
    version='0.3.1',
    description='Delayed/soft assertions for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='pr4bh4sh',
    url='https://github.com/pr4bh4sh/python-delayed-assert',
    packages=['delayed_assert'],
)
