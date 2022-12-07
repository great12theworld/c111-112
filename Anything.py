import os
import shutil

from_dir = "C:/Users/patil/Downloads/112/image_files"
to_dir = "C:/Users/patil/Downloads/112/image_files"

list_off_files = os.listdir(from_dir)

for file_name in list_off_files: 
    name,extention = os.path.splitext(file_name)
    if extention == '':
        continue
    if extention in['.gif','.js','.mp3','.py']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "image_files"
        path3 = to_dir + '/' + "image_files" + '/' + file_name


        if os.path.exists(path2):
            print("moving" + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving" + file_name + "...")
            shutil.move(path1,path3)