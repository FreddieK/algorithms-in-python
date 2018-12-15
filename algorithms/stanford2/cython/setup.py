from distutils.core import setup
from Cython.Build import cythonize

setup(name='Knapsack Loop',
      ext_modules=cythonize("knapsack_loop.pyx"))