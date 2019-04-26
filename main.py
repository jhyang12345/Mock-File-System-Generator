import sys, os
from optparse import OptionParser
from util import reduce_file_path, create_and_return_directory
from generate_file_system import generate_files
from pathlib import Path

def main(argv):
    parser = OptionParser()
    parser.add_option("-d", "--destination", dest="destination")
    parser.add_option("-c", "--count", dest="count")
    options, args = parser.parse_args()
    
    home = Path.home()
    destination = create_and_return_directory(reduce_file_path([home, "Documents", "test_directory"]))    
    d_only = False
    f_only = False
    count = 100
    if options.destination:
        destination = options.destination
    if options.count:
        count = int(options.count)

    generate_files(destination, count=count, is_directory=True)
    generate_files(destination, count)
    

if __name__ == '__main__':
    main(sys.argv[1:])