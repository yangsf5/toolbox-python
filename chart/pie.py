#!/usr/bin/python
# Author: sheppard(ysf1026@gmail.com) 2014-04-03

import getopt
from pychartdir import *
import sys

def usage():
    print 'usage:'
    print '-h\n\thelp'
    print '-i input file name'
    print '-o output png name'
    sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hi:o:')
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-i':
            input_name = arg
        elif opt == '-o':
            output_name = arg

    try:
        input_name
        output_name
    except:
        usage()

    draw(input_name, output_name)

def draw(in_name, out_name):
    in_f = file(in_name)

    labels = []
    data = []
    while True:
        line = in_f.readline()
        if len(line) == 0:
            break
        fields = line.split(' ')
        labels.append(fields[0])
        data.append(int(fields[1]))

    in_f.close()

    c = PieChart(2000, 1000)
    c.setPieSize(1000, 450, 400)
    c.setData(data, labels)
    c.makeChart(out_name)

if __name__ == '__main__':
    main(sys.argv[1:])
