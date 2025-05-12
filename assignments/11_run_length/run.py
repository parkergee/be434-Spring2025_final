#!/usr/bin/env python3
"""
Author : parker <parkergeffre@arizona.edu>
Date   : 2025-05-06
Purpose: Strings of DNA using [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) where runs of the same base (homopolymers) are represented by the base followed by a numeral representing the number of repetitions.
"""

import argparse
import sys
import os



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Import DNA string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        nargs='?',
                        help='DNA text or file')


    args = parser.parse_args()

    return args

# --------------------------------------------------
def rle(seq):
    """Run-length encode a DNA sequence"""
    count = 0
    prev_char = seq[0]
    rle_str = ''
    for char in seq:
        if char == prev_char:
            count += 1
        else:
            rle_str += prev_char                
            if count > 1: 
                    rle_str += f'{count}'
            prev_char = char
            count = 1
    rle_str += prev_char
    if count > 1:
                    rle_str += f'{count}'
    return rle_str
# --------------------------------------------------
def main():
    """Import DNA string"""
    args = get_args()

    f = args.seq
    
    if os.path.isfile(f):
        name = os.path.basename(f).replace('.txt','')
        file = open(f, 'rt')
        out_f = open('./expected/'+ name + '.out', 'wt')
        for line in file:
            dna = line.strip().upper()
            out_f.write(rle(dna)+'\n')
        out_f.close()
        file.close()

    else:
        dna = f.strip().upper()
        out_f = open('./expected/'+ dna + '.out', 'wt')
        out_f.write(rle(dna)+'\n')
        out_f.close()

        

# --------------------------------------------------
if __name__ == '__main__':
    main()
