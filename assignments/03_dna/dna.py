#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-16
Purpose: Add Your Purpose
"""

import argparse
from collections import Counter
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-file',
                        metavar= 'FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin],
                        help='Input DNA file(s)')

    return parser.parse_args()

                    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    t_DNA = args.dna
    t_file = args.file
    bp = ["A", "C", "G", "T", "a", "c", "g", "t"]
    for line in t_file:
        for char in line:
            if char in bp:
                print(char, end='')
            else:
                print()
                break


# --------------------------------------------------
if __name__ == '__main__':
    main()
