# For sorting and arranging files into subfolders based on file type #

# Author: Pratiksha Jain
# Created On: 13.06.21

#-------------------------------#
# Importing required libraries
import os
import glob
import shutil

#-------------------------------#
# Edit the exact folder name here, with path 
folder = "/home/folder/name/"

#-------------------------------#

# Dictionary of types of folders and the document extensions - if needed, edit according to your needs

filename = glob.glob(folder+"*")
doctype_dict = {
    'pdfs':['.pdf', '.PDF'],
    'docs':['.docx','.doc','.txt', '.ppt', '.pptx', '.md'],
    'images':['.jpeg','.jpg','.JPG','.svg','.png','.PNG', '.gif', '.psd'],
    'videos' : ['.mp4','.mp3', '.flb'],
    'setupFiles':['.exe','.msi', '.apk', '.EXE'],
    'compressedFiles':['.zip', '.rar'],
    'python codes': ['.py'],
    'setupFiles_Debian':['.deb'],
    'spreadsheets':[ '.xls', '.xlsx', '.csv', '.ods']
}

#-------------------------------#

# The actual code 

for file in filename:

    # getting extension of file
    f = os.path.splitext(file)[1]

    # Matching extension with dict values
    for key, value in doctype_dict.items():
        if f in value:
            
            # Defining location of subfolder
            loc = folder+key

            # in case subfolder does not exist already
            if not (os.path.exists(loc)):
                os.mkdir(loc)

            # moving file into subfolder
            shutil.move(file,loc)
            break

#-------------------------------#