#!/usr/bin/env python
"""Multipies the content of an XML file for testing purposes.

"""
import sys
import argparse
import random
import xml.etree.ElementTree as ET

_outputfile = 'multiplied.xml'

def setOutputFile(inputfile):
    """Determines the name of the output file
    

    """
    global _outputfile
    dot = inputfile.rfind('.')
    if dot > 0:
        _outputfile = inputfile[:dot] + '.multiplied' + inputfile[dot:]
    else:
        _outputfile = inputfile + '.multiplied'
    
def copyRoot(inputfile, copies):
    """Copies the root element of the input xml multiple times.
    
    """
    tree = ET.parse(inputfile)
    root = ET.tostring(tree.getroot())
    
    f = open(_outputfile, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>') 
    f.write('<multiplied>')
    for i in range(1, copies):
        f.write(root)
        f.write('\n')
    f.write('</multiplied>')
    f.close

    print 'Created ' + str(copies) + ' copies in ' + _outputfile
    
def copyElement():
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='source xml to multiply')
    parser.add_argument('-copies', default=2, 
                        help='the number root element copies (default=2)')
    parser.add_argument('-root', default=True, 
                        help='copy the root element (default=true)')
    args = parser.parse_args()
    
    setOutputFile(args.file)
    
    if args.root:
        copyRoot(args.file, int(args.copies))
    else:
        print 'Unfortunately this option is not supported yet.'
    
    