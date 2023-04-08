'''
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('xgboost')
'''
import tensorflow as tf
import pandas as pd
import numpy as np
import math
from xgboost import XGBClassifier
print("hello world")