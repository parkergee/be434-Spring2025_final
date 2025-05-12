#!/usr/bin/env python3
"""
Author : parker
Purpose: Blastomatic: Parsing Delimited Text Files
"""

import argparse
import csv
import os
import sys


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description=' BLAST hits above a given percent ID and merge them with annotations and print the query sequence ID',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                       '--blasthits',
                       help='BLAST -outfmt 6',
                       metavar='FILE',
                       type=str,
                       required=True)

    parser.add_argument('-a',
                       '--annotations',
                       help='Annotations file',
                       metavar='FILE',
                       type=str,
                       required=True)

    parser.add_argument('-o',
                       '--outfile',
                       help='Output file',
                       metavar='FILE',
                       type=str,
                       default='out.csv')

    parser.add_argument('-d',
                       '--delimiter',
                       help='Output field delimiter',
                       metavar='DELIM',
                       type=str,
                       default='')

    parser.add_argument('-p',
                       '--pctid',
                       help='Minimum percent identity',
                       metavar='PCTID',
                       type=float,
                       default=0.0)

    args = parser.parse_args()

    for file in [args.blasthits, args.annotations]:
        if not os.path.isfile(file):
            parser.error(f"No such file or directory: '{file}'")

    return args


def read_metadata(file):
    """Read the metadata file"""
    metadata = {}
    with open(file) as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            sys.exit(f"The file '{file}' is missing a header line.")
        if 'seq_id' not in reader.fieldnames:
            sys.exit(f"No 'seq_id' field found in '{file}'")

        for row in reader:
            metadata[row['seq_id']] = row
    return metadata


def guess_delimiter(filename, user_delim):
    """Guess the delimiter based on file extension"""
    if user_delim:
        return user_delim
    if filename.endswith(('.tsv', '.tab', '.txt')):
        return '\t'
    return ','


def get_blast_headers():
    """Return standard BLAST -outfmt 6 headers"""
    return ['seq_id', 'subject', 'pident', 'length', 'mismatch', 'gapopen',
            'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

def main():
    """Annotate BLAST hits"""
    args = get_args()
    metadata = read_metadata(args.annotations)
    results = []

    # BLAST output fields
    blast_headers = ['seq_id', 'subject', 'pident', 'length', 'mismatch', 'gapopen',
                    'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

    with open(args.blasthits) as fh:
        reader = csv.DictReader(fh, fieldnames=blast_headers, delimiter=',')
        for row in reader:
            query_id = row['seq_id']
            pct_id = float(row['pident'])

            if pct_id < args.pctid:
                continue

            if query_id not in metadata:
                continue

            results.append({
                'seq_id': query_id,
                'pident': row['pident'],
                'depth': metadata[query_id]['depth'],
                'lat_lon': metadata[query_id]['lat_lon']
            })

    delimiter = guess_delimiter(args.outfile, args.delimiter)
    with open(args.outfile, 'w', newline='') as out_fh:
        writer = csv.DictWriter(
            out_fh,
            fieldnames=['seq_id', 'pident', 'depth', 'lat_lon'],
            delimiter=delimiter)
        writer.writeheader()
        writer.writerows(results)

    print(f'Exported {len(results)} to "{args.outfile}".')


if __name__ == '__main__':
    main()