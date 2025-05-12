#!/usr/bin/env python3
"""
Author : parker <Add your email>
Date   : 2025-05-06
Purpose: test
"""

import argparse
import os
import sys
import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
        nargs='+',
        metavar='FILE',
        type=argparse.FileType('rt'),
        help='Input FASTA file(s)')
    
    parser.add_argument('-t',
        '--tablefmt',
        help='Table format',
        metavar='str',
        type=str,
        default='simple',
        choices=tabulate.tabulate_formats)

    args = parser.parse_args()

    for file in args.file:
        if not os.path.isfile(file.name):
            parser.error(
                f"No such file or directory: '{file}'"
            )

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.file
    table = []
    
    for fh in seq:
        num_seqs = 0
        min_len = float('inf')
        max_len = 0
        avg_len = 0
        total_len = 0
        name = os.path.relpath(fh.name)
        for line in fh:
            if line.startswith('>'):
                              num_seqs += 1
                              #print(line.strip())
            else:
                total_len += len(line.strip())
                min_len = min(min_len, len(line.strip()))
                max_len = max(max_len, len(line.strip()))
                avg_len = total_len / num_seqs
             
        table.append([name, min_len, max_len, avg_len, num_seqs])

    print(tabulate.tabulate(table, headers=['name', 'min_len', 'max_len', 'avg_len', 'num_seqs'], tablefmt=args.tablefmt))
# --------------------------------------------------
if __name__ == '__main__':
    main()
