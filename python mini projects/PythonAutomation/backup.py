import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/USER/Pictures/Images"
destination_dir = "C:/Users/USER/Documents/ebuka's web development project/python mini project/PythonAutomation/Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"folder already exists in: {dest}")

schedule.every().day.at("17:19").do(lambda: (copy_folder_to_directory(source_dir, destination_dir)))

while True:
    schedule.run_pending()
    time.sleep(60)

