import sys
import os
from datetime import datetime
import shutil

# enter the path of the folder of which files you want to organize and make sure to save this file in this path itself
directory = f'path'

# loop through the files in the directory path
for filename in os.listdir(directory):
    # enter the extension f the files which you to organize
    if filename.endswith('.py'):
        # get the modified date of the file as timestamp
        modified = os.stat(f'{directory}/{filename}').st_mtime
        # convert the timestamp date into human readable date
        modified_date = datetime.fromtimestamp(modified)

        # get the year from the modified date
        year = modified_date.strftime("%Y")

        # get the month from the modified date
        month = modified_date.strftime("%B")

        # get the date from the modified date
        date = modified_date.strftime(f"%m-%d-%Y")

        # create the year folder if not exists
        if not os.path.exists(year):
            os.mkdir(year)

        # create the month folder if not exists
        if not os.path.exists(f"{year}/{month}"):
            os.mkdir(f"{year}/{month}")

        # create the date folder if not exists
        if not os.path.exists(f"{year}/{month}/{date}"):
            os.mkdir(f"{year}/{month}/{date}")

        # move files one by one, print is ptional
        print(shutil.move(filename, f'{directory}/{year}/{month}/{date}'))
