#!/usr/bin/env python3
"""
Author : Parker Geffre - parkergeffre@arizona.edu
Date   : 2025-02-02
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        default = 'Howdy',
                        metavar='greeting',
                        help='The greeting')
    
    parser.add_argument('-n',
                        '--name',
                        default = 'Stranger',
                        metavar='name',
                        help='Whom to greet')
    
    parser.add_argument('-e',
                        '--excited',
                        action = "store_true",
                        help='Include an exclamation point')

    return parser.parse_args()


# --------------------------------------------------
def main(): 
    """main"""
    args = get_args()
    greeting = args.greeting
    name = args.name
    ex = args.excited
    end = "!" if ex else "."
        
        
    
    print(f"{greeting}, {name}{end}")

# --------------------------------------------------
if __name__ == '__main__':
    main()
