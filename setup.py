from setuptools import setup, find_packages
import version

setup(
    name='samana',
    version=version.VERSION,
    packages=find_packages(include=['samana', 'samana.*']),
    install_requires=[ 'urllib3' ]
)