import os
import sys
import warnings
import scipy as sp
import sklearn as sk
import matplotlib as matplt

#supress Tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
import warnings

warnings.filterwarnings('ignore') # Ignores all warnings
# Specific warning types can be ignored by specifying the category
#warnings.filterwarnings('ignore', category=DeprecationWarning)
import logging
logging.getLogger('tensorflow').disabled = True


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


try:
  import torch;
  print("Torch version#:{:>12}".format(torch.__version__))
except ImportError as e:
  print("ERROR:  Importing Torch, " + str(e))
  print("Please install tensorflow library and check your PATH and PYTHONPATH variables.")
  sys.exit(1) 


try:
  print("")
  gpu_count=0
  current_gpu=""
  num_cpus_torch = torch.get_num_threads()
  if torch.cuda.is_available():
      gpu_count=torch.cuda.device_count()
      current_gpu=torch.cuda.get_device_name(0)
      device=torch.device("cuda")
  else:
      device=torch.device("cpu")
  print(f"Torch System Report.")
  print("Num GPUs Available: " + str(gpu_count))
  print("         GPUs Name: " + str(current_gpu))
  print("Num CPUs Available: " + str(num_cpus_torch))

except Exception as e:
  print("ERROR:  Importing Torch, " + str(e))
  print("Please install tensorflow library and check your PATH and PYTHONPATH variables.")
  sys.exit(1) 
