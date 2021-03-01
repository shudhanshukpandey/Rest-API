from setuptools import setup, find_packages


setup(
    name="foo",
    version="1.0",
    package=find_packages(),
    install_requires=['Flask','googletrans']

)