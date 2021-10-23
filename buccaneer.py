import tkinter as tk
import os

os.chdir("/home/slater/store/coding/buccaneer/")

test_dir = "/home/slater/store/Music/"

with open('dirlist.txt') as dirlist:
    lines = dirlist.readlines()

print(lines)

def list_inodes(directory):
    read_list = []
    for inode in os.scandir(directory):
        if inode.is_file():
            read_list.append(inode)
        else:
            read_list += list_inodes(inode)
    return read_list

def list_files(inodes_list):
    files_list = []
    for inode in inodes_list:
        if inode.is_file:
            files_list.append(inodes_list)
    return files_list

def names_list_from_files_list(files_list):
    names_list = []
    for nameable in files_list:
        names_list.append(nameable.name)
    return names_list

def convert_file(file, output_format):
    output_file_name = file.path.split(".")[0] + output_format
    # command = ["ffmpeg", "-i", file.path, file.path + output_format]
    # command = f"ffmpeg -i {file.path} {file.path}.{output_format}"
    # subprcss = subprocess.run([command])
    # print(command)
    # #it needs to rpint the command
    pass

def start_convert(file_list, output_format):
    for file in file_list:
        convert_file(file, output_format)

test_list = list_inodes("/home/slater/store/Music/")
print(list_files(test_list))

# for directory in lines:
#     directory = directory[:-1]
#     print(directory)
#     for file in os.scandir(directory):
#         print(file.is_file())

for directory in lines:
    print(list_inodes(directory[:-1]))

#['__class__', '__class_getitem__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__fspath__', '__ge__', '__getattribute__', 
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'inode', 'is_dir', 'is_file', 'is_symlink', 'name', 'path', 'stat']
