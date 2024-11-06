from setuptools import setup, find_packages

setup(
    name='Biblioteca',
    version='0.1',
    packages=find_packages(),
    description='Uma biblioteca comum',
    install_requires=[
        "requests",
    ]
)