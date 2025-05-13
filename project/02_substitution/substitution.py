#!/usr/bin/env python3
"""
Author : parker <Add your email>
Date   : 2025-01-24
Purpose: Add Your Purpose
"""

import argparse
import os
import sys
import random

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

    parser.add_argument('-s', 
        '--seed',
        help='Random seed for reproducible keys',
        metavar='SEED',
        type=int,
        default=3)
    
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
def gen_random(seed):
    """Generate a random substitution cipher key"""
    if seed is not None:
        random.seed(seed)

    # Create list of uppercase letters
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Shuffle the alphabet to create the cipher key
    shuffled = alphabet.copy()
    random.shuffle(shuffled)

    return ''.join(shuffled)

# --------------------------------------------------
def SUBen(seed, file):
    """Encode text using the substitution cipher"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    shuff = gen_random(seed)
    for line in file:
        line = line.strip()
        for char in line:
            upper_char = char.upper()
            if upper_char in alpha:
                # Find position in normal alphabet and substitute with cipher character
                index = alpha.index(upper_char)
                result += shuff[index]
            else:
                # Non-alphabetic characters remain unchanged
                result += char
    print(result)
    
    return result

# --------------------------------------------------
def SUBde(seed, file):
    """Encode text using the substitution cipher"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    shuff = gen_random(seed)
    for line in file:
        line = line.strip()
        for char in line:
            upper_char = char.upper()
            if upper_char in alpha:
                # Find position in normal alphabet and substitute with cipher character
                index = shuff.index(upper_char)
                result += alpha[index]
            else:
                # Non-alphabetic characters remain unchanged
                result += upper_char
    print(result)

    return result

# --------------------------------------------------
def main():
    """ENCODE/DECODE"""

    args = get_args()
    f = os.path.relpath(args.file.name)
    file = open(f, 'rt')
    name = os.path.basename(file.name)
    seed = args.seed
    if args.outfile:
        out_f = open('./outputs/' + args.outfile +'.txt', 'wt')
    else:
        out_f = open('./outputs/' + name, 'wt') 

    if args.decode:
        out_f.write(SUBde(seed, file) + '\n')
        #print(SUBde(seed,file))
        out_f.close()
        file.close()
        #print(f'Done, wrote decoded {name} to directory "outputs".')
    else:
        out_f.write(SUBen(seed, file) + '\n')
        #print(SUBen(seed, file))
        out_f.close()
        file.close()
        #print(f'Done, wrote encoded {name} to directory "outputs".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
