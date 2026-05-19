import shutil
import os
import time

BASE=os.path.expanduser("~/HUDA_SOVEREIGN_RUNTIME")
BACKUP=os.path.expanduser("~/HUDA_BACKUP_RUNTIME")

while True:

    try:
        shutil.copytree(BASE,BACKUP,dirs_exist_ok=True)
    except:
        pass

    time.sleep(300)
