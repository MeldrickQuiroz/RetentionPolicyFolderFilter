import os, shutil, datetime, time
from datetime import date

def get_folder_size(source_folder, destination_folder, RetentionDays):

    todayDate = date.today()
    deltaDate = datetime.timedelta(int(RetentionDays))
    pastRetention = todayDate - deltaDate
    Foldersize = float(100)

    for directory in os.listdir(source_folder):
        inner_full_path = os.path.join(source_folder, directory)
        total_size = 0
        print(inner_full_path)

        for dirpath, dirnames, filenames in os.walk(inner_full_path):

            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)

        fileInfo = os.stat(inner_full_path)
        fileTime = fileInfo.st_birthtime
        creation = time.strftime('%m %d %Y', time.gmtime(fileTime))
        created_date = datetime.datetime.strptime(creation, '%m %d %Y').date()
        sizeGB = total_size / (1024 * 1024 * 1024)
        
        if created_date < pastRetention and sizeGB > Foldersize:
            shutil.move(inner_full_path, destination_folder)


src_path = input ("Enter the source path: ")
dst_path = input("Enter destination folder path: ")
retentionPolicy = input("Enter retention policy: ")

size = get_folder_size(src_path, dst_path, retentionPolicy)
