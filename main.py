import sys, os
from optparse import OptionParser
from util import reduce_file_path, create_and_return_directory

def main(argv):
    parser = OptionParser()
    parser.add_option("-d", "--destination", dest="destination")
    options, args = parser.parse_args()
    
    destination = create_and_return_directory(reduce_file_path(["~", "Documents", "test_directory"]))
    d_only = False
    f_only = False
    count = 100
    if options.destination:
        destination = options.destination    


if __name__ == '__main__':
    main(sys.argv[1:])