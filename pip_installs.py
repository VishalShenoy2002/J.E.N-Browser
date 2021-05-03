import os
import sys

os.system('cd {}'.format(sys.path[6]))

for package in ['pip uninstall PyQt5','pip uninstall PyQtWebEngine']:
    os.system(package)
    print('Installation Done')
    
