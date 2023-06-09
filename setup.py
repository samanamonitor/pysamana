from setuptools import setup, find_packages
from samana import __version__
import re

def set_control_version():
    with open("./debian/control.tmpl", "r") as src, open("./debian/control", "w") as dst:
        while True:
            datain = src.readline()
            if len(datain) == 0: break
            dataout = re.sub(r"%VERSION%", __version__, datain)
            dst.write(dataout)

if __name__ == "__main__":
    set_control_version()
    setup(
        name='samana',
        version=__version__,
        packages=find_packages(include=['samana', 'samana.*']),
        install_requires=[ 'urllib3' ]
    )
