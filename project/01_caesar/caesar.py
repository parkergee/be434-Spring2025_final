#!/usr/bin/env python3
"""
Author : parker <Add your email>
Date   : 2025-01-24
Purpose: Add Your Purpose
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Caesar Shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        help='Input file',
        metavar='FILE',
        #nargs='?',  #how to do without args
        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A named integer argument to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3, 
                        required= True)
    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type= str,
                        default='')

    args = parser.parse_args()

    if not os.path.isfile(args.file.name):
        parser.error(f"No such file or directory: '{args.file.name}'")

    return args


# --------------------------------------------------
def CSRen(file):
    args = get_args()
    """ENCODE CEASAR SHIFT"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = ''
    for line in file:
        for char in line:
            if char in alpha:
                encoded += alpha[(alpha.index(char) + args.number) % 26]
                #print(encoded)
            else:
                encoded += char
                #print(encoded)

    return encoded


# --------------------------------------------------
def CSRde(file):
    args = get_args()
    """DECODE CEASAR SHIFT"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decoded = ''
    for line in file:
        for char in line:
            if char in alpha:
                decoded += alpha[(alpha.index(char) - args.number) % 26]
                #print(decoded)
            else:
                decoded += char
                #print(decoded)

    return decoded


# --------------------------------------------------
def main():
    """ENCODE/DECODE"""

    args = get_args()
    f = os.path.relpath(args.file.name)
    file = open(f, 'rt')
    name = os.path.basename(file.name)
    if args.outfile:
        out_f = open('./outputs/' + args.outfile +'.txt', 'wt')
    else:
        out_f = open('./outputs/' + name, 'wt') 

    if args.decode:
        for line in file:
            fmt = line.strip().upper()
            out_f.write(CSRde(fmt) + '\n')
            print(CSRde(fmt))
        out_f.close()
        file.close()
        #print(f'Done, wrote decoded {name} to directory "outputs".')
    else:
        for line in file:
            fmt = line.strip().upper()
            out_f.write(CSRen(fmt) + '\n')
            print(CSRen(fmt))
        out_f.close()
        file.close()
        #print(f'Done, wrote encoded {name} to directory "outputs".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
