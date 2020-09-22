import sys
import os

# enter the path of the folder of which files you want to open
directory = f'path'
# loop through the files in the directory path
for filename in os.listdir(directory):
    #  enter the extension f the files which you to open
    # if filename.endswith('.xlsx') or filename.endswith('.docx'):
    os.startfile(f'{directory}/{filename}')

# paths for applications to open
os.startfile(f'path')
