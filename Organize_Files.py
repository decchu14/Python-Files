import sys
import os
from datetime import datetime
import shutil

directory = f'path'


for filename in os.listdir(directory):
    # date = time.ctime(os.path.getctime(f'{directory}/{filename}')).py
    if filename.endswith('.py'):
        created = os.stat(f'{directory}/{filename}').st_ctime
        modified_date = datetime.fromtimestamp(created)
        year = modified_date.strftime("%Y")
        month = modified_date.strftime("%B")
        date = modified_date.strftime(f"%m-%d-%Y")
        if not os.path.exists(year):
            os.mkdir(year)
        if not os.path.exists(f"{year}/{month}"):
            os.mkdir(f"{year}/{month}")
        if not os.path.exists(f"{year}/{month}/{date}"):
            os.mkdir(f"{year}/{month}/{date}")
        print(shutil.move(filename, f'{directory}/{year}/{month}/{date}'))
        # month = modified_date.strftime("%B")
        # if not os.path.exists(month):
        #     os.mkdir(month)
