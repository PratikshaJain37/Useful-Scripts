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
folder = "/home/folder/name"

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
    file_base = file.replace(folder,'')
    ext = os.path.splitext(file_base)[1]

    # Matching extension with dict values
    for key, value in doctype_dict.items():
        if ext in value:
            
            # Defining location of subfolder
            loc = folder+key

            # in case subfolder does not exist already
            if not (os.path.exists(loc)):
                os.mkdir(loc)

            # moving file into subfolder
            try:
            	shutil.move(file,loc)
            except shutil.Error as e:
                print(e.args[0])

                # Error: File with same name already exists in that folder
                if 'already exists' in e.args[0]:
                    file_1 = file.replace(ext, '_1'+ext)
                    os.rename(file, file_1)
                    shutil.move(file_1,loc)
                    print("File can be found as %s_1"%file_base.replace(ext,''))
                    

            break

#-------------------------------#
