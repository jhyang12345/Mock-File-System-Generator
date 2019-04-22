import sys, os
import shutil

def create_and_return_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
