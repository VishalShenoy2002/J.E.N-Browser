import os
import sys

os.system('cd {}'.format(sys.path[5]))

for package in ['pip install PyQt5','pip install PyQtWebEngine']:
    os.system(package)
    print('Installation Done')
    
