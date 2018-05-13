from setuptools import setup
from distutils.core import setup
import distutils.sysconfig as c
import py2app
import codecs # Allows to load a file containing UTF-8 characters
import matplotlib.pyplot as plt # Allows to create graphics, especially those in 3D
import matplotlib as mpl # Allow to use matplotlib to make graphs
import numpy as np # Allows to manipulate the necessary table for sklearn
import os # Allows to modify some things on the os
import random # Allows to use random variables
import shutil #permet la copie de fichier
import sys # Allow to modify files on the OS
import tkFont # Allows to modify the TKinter display font
import Tkinter as tk # Allows the TKinter database with the abreviation tk
import tkFileDialog  # Allows to create a windows to load files
import webbrowser
import matplotlib
import matplotlib.backends.backend_tkagg
import sklearn
import Tkinter
from scipy.sparse.csgraph import _validation
from scipy.special import _ufuncs_cxx
#from cx_Freeze import setup, Executable
OPTIONS={'argv_emulation': True}
# On appelle la fonction setup
setup(
    app=['projetfinal.py'],
    name = "Neuron Classification",
    version = "1",
    description = "Classification of neurons through Machine Learning",
    #console = ["projetfinal.py"],
    #data_files=matplotlib.get_py2exe_datafiles(),
    options={"py2exe":{'py2app':OPTIONS,'includes':r'libpython2.7.dylib'}},
    setup_requires=['py2app'],
)
#r'includes':[r'scipy.sparse.csgraph._validation',r'scipy.linalg.cython_blas',r'scipy.linalg.cython_lapack', r'scipy.special._ufuncs_cxx',r'scipy._lib.messagestream',r'scipy._lib.messagestream',r'sklearn.utils.lgamma',r'sklearn.utils.weight_vector',r'sklearn.neighbors.typedefs',r'os'],