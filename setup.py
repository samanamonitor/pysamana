from setuptools import setup, find_packages
import version

setup(
    name='samana',
    version='0.0.1,
    packages=find_packages(include=['samana', 'samana.*']),
    install_requires=[ 'urllib3' ]
)