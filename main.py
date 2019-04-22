import sys, os
from optparse import OptionParser

def main(argv):
    parser = OptionParser()
    parser.add_option("-d", "--destination", dest="destination")
    option, args = parser.parse_args()
    
    destinations = ""
    d_only = False
    f_only = False
    count = 100
        

if __name__ == '__main__':
    main(sys.argv[1:])