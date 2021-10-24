import tkinter as tk
import subprocess
import os

dirs_from_dirlist = []

format_extensions = {"vorbis": "ogg", "m4a": "m4a", "mp3": "mp3", "flac": "flac"}

# handles all of the information required for conversion, as well as the conversion process
class Conversion:
    def __init__(self, input_path, format_, output_method, *options):
        self.input_path = input_path
        self.format_ = format_
        self.output_method = output_method
        self.options = options

    #converts files
    #options passed are ffmpeg options
    def convert(self):
        return subprocess.Popen(["ffmpeg", "-i", self.input_path, *self.options, self.output_method(self.input_path, self.format_)], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

# open file containing directories and ignore entries beginning with "#"
with open('dirlist.txt') as dirlist:
    for line in dirlist.readlines():
        if line[0] != "#":
            dirs_from_dirlist.append(line)

def remove_file_extension(file_string):
    return os.path.splitext(file_string)[0]

# deposits the output file in the same directory as the input, retains its name
def output_method_keep_name_path(input_path, output_format):
    return remove_file_extension(input_path) + "." + format_extensions[output_format]

# button method for a user confirming multiple conversions, placeholder
def button_lock_conversions(dirs, output_format, output_method, *options):
    conversions_list = []
    for dir in dirs:
        conversions_list.append(Conversion(dir.path, output_format, output_method, *options))
    convert_list(conversions_list)

# convert all conversions from a list
def convert_list(conversions_list):
    active_processes = []
    for conversion in conversions_list:
        while len(active_processes) > 5:
            for active_process in active_processes:
                if active_process.poll() != None:
                    active_processes.remove(active_process)
                    print("popen finished " + str(active_process))
        active_processes.append(conversion.convert())

# return inodes (files or folders) from a string pointing to a dir -> list of inodes of kind "DirEntry"
def list_inodes(directory):
    read_list = []
    for inode in os.scandir(directory):
        if inode.is_file():
            read_list.append(inode)
        else:
            read_list += list_inodes(inode)
    return read_list

# take a list of inodes of type "DirEntry" and return a list of files within
def list_files(inodes_list):
    return [inode for inode in inodes_list if inode.is_file]

# same as list_files() but with directories
def list_directories(inodes_list):
    return [inode for inode in inode_list if inode.is_dir]

# get all the names of files from a list of DirEntry's
def names_list_from_inodes_list(inodes_list):
    return [nameable.name for nameable in inodes_list]

#TESTS
#convert all items in a directory/subdirectories
def test_dirslist():
    file_list = list_files(list_inodes(dirs_from_dirlist[0])) #should work, does not
    button_lock_conversions(file_list, "vorbis", output_method_keep_name_path, "-vn")
