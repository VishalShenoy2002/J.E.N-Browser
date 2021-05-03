import os

for file in os.listdir(os.getcwd()):
    if os.path.isfile(os.getcwd()+'\\{}'.format(file)):
        if 'git' in file.lower() or file.endswith('.md')==False:
            os.system('git add {}'.format(file))