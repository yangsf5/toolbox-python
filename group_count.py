#!/usr/bin/python
# Author: sheppard(ysf1026@gmail.com) 2013-11-19

import commands
import getopt
import re
from sets import Set
import sys

def usage():
    print 'usage:'
    print '-h\n\thelp'
    print '-f filename\n\tparse this file'
    print '-r reg\n\tregex string, need \'\' or ""'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hf:r:')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-f':
            global _file_name
            _file_name = arg
        elif opt == '-r':
            global _reg
            _reg = arg

    stat()
            
def stat():
    reg = re.compile(_reg)
    args = Set()

    f = file(_file_name)
    while True:
        line = f.readline()
        if len(line) == 0:
            break

        ret = reg.search(line)
        if ret == None:
            pass
        else:
            args.add(ret.group())
    f.close()

    for arg in args:
        output = commands.getoutput('grep %s %s -c' % (arg, _file_name))
        print 'count of %s: %s' % (arg, output)


if __name__ == '__main__':
    main(sys.argv[1:])

