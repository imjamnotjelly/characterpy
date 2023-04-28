from setuptools import setup, find_packages
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="c_ai",
    version="1.0.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imjamnotjelly/characterpy",
    author="imjamnotjelly",
    packages=find_packages(include=['c_ai']),
)