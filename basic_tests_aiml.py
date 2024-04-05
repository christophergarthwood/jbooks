import os
import sys
import warnings
import scipy as sp
import sklearn as sk
import matplotlib as matplt

#supress Tensorflow warnings
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print("SciPy version     #:{:>12}".format(sp.__version__))
print("Sk-Learn version  #:{:>12}".format(sk.__version__))
print("Matplotlib version#:{:>12}".format(matplt.__version__))

print ("")
print (f"Importing Numpy, Pandas, and Tensorflow library.")
try:
  import numpy as np;
  print("Numpy version     #:{:>12}".format(np.__version__))
except ImportError as e:
  print("ERROR:  Importing Numpy, " + str(e))
  print("Please install Numpy library and check your PATH and PYTHONPATH variables.")
  sys.exit(1) 

try:
  import pandas as pd;
  print("Pandas version    #:{:>12}".format(pd.__version__))
except ImportError as e:
  print("ERROR:  Importing Pandas, " + str(e))
  print("Please install Pandas library and check your PATH and PYTHONPATH variables.")
  sys.exit(1) 


try:
  import tensorflow as tf;
  print("Tensorflow version#:{:>12}".format(tf.__version__))
except ImportError as e:
  print("ERROR:  Importing Tensorflow, " + str(e))
  print("Please install tensorflow library and check your PATH and PYTHONPATH variables.")
  sys.exit(1) 


try:
  print("")
  print(f"Tensorflow System Report.")
  print("Num GPUs Available: " + str(len(tf.config.experimental.list_physical_devices('GPU'))))
  print("Num CPUs Available: " + str(len(tf.config.experimental.list_physical_devices('CPU'))))
except Exception as e:
  print("ERROR:  Tensorflow API invocation error, " + str(e))
  sys.exit(1) 


