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

# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])  

