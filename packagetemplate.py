#!pip install setuptools

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="VictorVS",
    author_email="victor@test.com",
    description="This is my package template",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/VictorVdoS/bootcamp_dio/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)