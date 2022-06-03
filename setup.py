import os
import py2exe
from distutils.core import setup

setup(console=['machsim/main.py'])
os.rename('dist/main.exe','dist/machine-simulator.exe')
