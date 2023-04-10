from setuptools import setup, find_packages
from samana import __version__

setup(
    name='samana',
    version=__version__,
    packages=find_packages(include=['samana', 'samana.*']),
    install_requires=[ 'urllib3' ]
)