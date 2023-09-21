# Google drive backup

# List files in google drive
# Download files from google drive

# pip install pydrive

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1LNoUbIv4YSMsIm5gAZPqKXGHD6ejM2nL'

# Delete Files
fileList = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()

for e in fileList:
    drive.CreateFile({'id': e['id']}).Trash()
    # drive.CreateFile({'id': e['id']}).Delete()