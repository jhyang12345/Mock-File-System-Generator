import sys, os, time
import shutil

def create_and_return_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def reduce_file_path(path_list):
    ret = ""
    for p in path_list:
        ret = os.path.join(ret, p)
    return ret