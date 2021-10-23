import tkinter as tk
import os

dirs_from_list = []

with open('dirlist.txt') as dirlist:
    for line in dirlist.readlines():
        print(line)
        if line[0] != "#":
            dirs_from_list.append(line)

#return inodes (files or folders) -> list of inodes of kind "DirEntry"
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

#get all the names of files from a list of DirEntry's
def names_list_from_files_list(files_list):
    names_list = []
    for nameable in files_list:
        names_list.append(nameable.name)
    return names_list

#take in a list of DirEntry's and reformats to pass them to conversion function(s)
def start_convert_files(file_list, output_format):
    pass

#final step of file conversion process
def convert_file(file, output_format):
    output_file_name = file.path.split(".")[0] + output_format
    pass

# test_list = list_inodes(dirs_from_list[0])
# print(list_files(test_list))

# for directory in dirs_from_list:
#     print(list_inodes(directory[:-1]))

#['__class__', '__class_getitem__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__fspath__', '__ge__', '__getattribute__', 
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'inode', 'is_dir', 'is_file', 'is_symlink', 'name', 'path', 'stat']
