import os

## SERVER
# PATH_TO_FOLDER = '/home/cst/Jixie/source code/unit_forecasting/'
PATH_TO_FOLDER = str(os.getcwd())+'/'
print(PATH_TO_FOLDER)

VERSION = '0.1.0'

RANDOM_STATE = 42

# tree setting
MAX_DEPTH=3
MIN_SAMPLES_LEAF=100
CCP_ALPHA=0.001