import os
import io
from setuptools import setup


setup(
    name='delayed_assert',
    version='0.3.5',
    description='Delayed/soft assertions for python',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='pr4bh4sh',
    url='https://github.com/pr4bh4sh/python-delayed-assert',
    packages=['delayed_assert'],
)
