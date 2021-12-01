import subprocess as sp
import os
from collections.abc import Callable

dirs_from_dirlist: list[str] = []
# open file containing directories and ignore entries beginning with "#"
with open('dirlist.txt') as dirlist:
    for line in dirlist.readlines():
        if line[0] != "#":
            dirs_from_dirlist.append(line)


format_extensions: dict[str, str] = {"vorbis": "ogg",
                                     "m4a": "m4a",
                                     "mp3": "mp3",
                                     "flac": "flac"} # expand this

conversion_methods: dict[str, str] = {"keep name": "keepnamefunction()",
                                      "leave where found": "leavewherefoundfunction()",
                                      "exif subdirectories": "exifsubdirectories(args)",
                                      "delete original": "deleteoriginal()"}

# handles all of the information required for conversion, as well as the conversion process
class Conversion:
    def __init__(self, input_path: str, output_format: str, output_method: Callable[[str, str], str], *options: str):
        self.input_path = input_path
        self.output_format = output_format
        self.output_method = output_method
        self.options = options

    def __repr__(self):
        return (f"Input method: {self.input_path}\n"
                f"Output format: {self.output_format}\n"
                f"Output method: {self.output_method}\n"
                f"Options: {self.options}")

    def convert(self) -> sp.Popen:
        """The main call to ffmpeg"""
        ffmpegoptions = ["ffmpeg",
                         "-i",
                         self.input_path,
                         *self.options,
                         self.output_method(self.input_path, self.output_format)]
        return sp.Popen(ffmpegoptions, stderr=sp.DEVNULL, stdout=sp.DEVNULL)

def remove_file_extension(file_string: str) -> str:
    """Removes the file extension from a path
    e.g. /path/to/obj.txt -> /path/to/obj"""
    return os.path.splitext(file_string)[0]

def output_method_keep_name_path(input_path: str, output_format: str) -> str:
    """Output method that places the output file in the same directory as the input, retaining its name, possibly with a different extension"""
    return remove_file_extension(input_path) + "." + format_extensions[output_format]

def button_lock_conversions(dirs: list[os.DirEntry], output_format: str, output_method: Callable[[str, str], str], *options: str) -> None:
    """PLACEHOLDER
    Button method for a user confirming multiple conversions"""
    conversions_list: list[Conversion] = []
    for dir in dirs:
        conversions_list.append(Conversion(dir.path, output_format, output_method, *options))
    #TODO: return conversions_list?
    convert_list(conversions_list)

def convert_list(conversions_list: list[Conversion]) -> None:
    """Convert all conversion from a list"""
    active_processes: list[sp.Popen] = []
    for conversion in conversions_list:
        while len(active_processes) > 5:
            for active_process in active_processes:
                if active_process.poll() != None:
                    active_processes.remove(active_process)
                    print("popen finished " + str(active_process)) # TESTING
        active_processes.append(conversion.convert())

def list_inodes(directory: str) -> list[os.DirEntry]:
    """Returns a flattened list of all inodes (files or folders) in a directory."""
    read_list: list[os.DirEntry] = []
    for inode in os.scandir(directory):
        if inode.is_file():
            read_list.append(inode)
        else:
            read_list += list_inodes(inode.path)
    return read_list

def list_files(inodes_list: list[os.DirEntry]) -> list[os.DirEntry]:
    """Filters a list of inodes, returning only a list of files."""
    return [inode for inode in inodes_list if inode.is_file]

def list_directories(inodes_list: list[os.DirEntry]) -> list[os.DirEntry]:
    """Filters a list of inodes, returning only a list of directories."""
    return [inode for inode in inodes_list if inode.is_dir]

def names_list_from_inodes_list(inodes_list: list[os.DirEntry]) -> list[str]:
    """Returns a list of names of all inodes in a list."""
    return [inode.name for inode in inodes_list]

#####TESTS
def test_dirslist() -> None:
    """Convert all items in a directory/subdirectories"""
    file_list: list[os.DirEntry] = list_files(list_inodes(dirs_from_dirlist[0])) #TODO: should work, does not
    button_lock_conversions(file_list, "vorbis", output_method_keep_name_path, "-vn")
