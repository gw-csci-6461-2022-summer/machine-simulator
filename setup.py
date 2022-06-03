import os
import py2exe
from distutils.core import setup

setup(console=['gui_grid.py'])
os.rename('dist/gui_grid.exe','dist/machine-simulator.exe')