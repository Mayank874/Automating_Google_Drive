# Google drive backup

# Upload files to google drive
# List files in google drive

# pip install pydrive
 
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1LNoUbIv4YSMsIm5gAZPqKXGHD6ejM2nL'

#Upload files
directory = "C:/Users/Mayank/OneDrive - Amity University/Desktop/Google Drive Application Project/data"
for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()


