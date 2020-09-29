import os
import shutil


src = f'enter the source path'
dst = f'enter the destination path'

# deleting the folder if it exists
if os.path.exists(dst):
    shutil.rmtree(dst, ignore_errors=True)

# copying folder from source to destination
shutil.copytree(src, dst)
