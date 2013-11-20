#!/usr/bin/python
# Author: sheppard(ysf1026@gmail.com) 2013-11-19

import commands
import getopt
import sys

def usage():
    print 'usage:'
    print '-h\n\thelp'
    print '-f filename\n\tparse this file'
    print 'arg arg arg ...'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hf:')
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

    global _args
    _args = args
    if len(_args) == 0:
        print 'error: args is empty'
        sys.exit(2)

    stat()
            
def stat():
    for arg in _args:
        output = commands.getoutput('grep %s %s -c' % (arg, _file_name))
        print 'count of %s: %s' % (arg, output)


if __name__ == '__main__':
    main(sys.argv[1:])

