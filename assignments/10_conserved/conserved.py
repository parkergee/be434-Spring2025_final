#!/usr/bin/env python3
"""
Author : parker
Purpose: Find conserved bases in aligned sequences
"""

import argparse
import os
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Input file')
    args = parser.parse_args()
    for file in [args.file]:
        if not os.path.isfile(file):
            parser.error(f"No such file or directory: '{file}'")

    return args
# --------------------------------------------------
def find_conserved(sequences):
    """Find conserved bases in aligned sequences"""
    if not sequences:
        return ''

    # Check all sequences have same length
    seq_len = len(sequences[0])
    if not all(len(seq) == seq_len for seq in sequences):
        return ''

    # Compare each position across all sequences
    conserved = []
    for i in range(seq_len):
        # Get all bases at this position
        bases = [seq[i] for seq in sequences]
        # If all bases match, mark with |, otherwise X
        conserved.append('|' if len(set(bases)) == 1 else 'X')

    return ''.join(conserved)

# --------------------------------------------------
def main():
    """Open file and print conserved bases"""
    args = get_args()

    # Read sequences from file
    sequences = []
    with open(args.file) as fh:
        for line in fh:
            if line.strip():  # Skip empty lines
                sequences.append(line.strip())

    # Print sequences
    for seq in sequences:
        print(seq)

    # Print conservation pattern
    print(find_conserved(sequences))

# --------------------------------------------------
if __name__ == '__main__':
    main()
