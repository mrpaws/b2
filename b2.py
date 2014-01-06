#!/usr/bin/env python

import sys
import argparse

class Translator():
   pass

def read_stdin():
    product=""
    for line in sys.stdin:
        product = "{p}{l}".format(
            p = product, 
            l = line
            )
    return product[:-1]

def manage_cli_args():
    parser = argparse.ArgumentParser(
        description="Translate base2 & base10",
        usage = "%(prog)s <number> [-hv]"
        )
    parser.add_argument(
        'number',
        nargs='?',
        type = int,
        help = "either a binary or decimal number",
        default = sys.stdin
        )
    parser.add_argument(
        '-v',
        '--verbose',
        help = "return verbose output",
        action = 'store_true',
        default = False
        )
    args = parser.parse_args()

    verbosity = args.verbose
    uinput = args.number
    verbosity = args.verbose

    uinput_type = type(uinput)
    if uinput_type is file:
        uinput = sys.stdin.read()[:-1]
        try: 
            uinput = int(uinput)
        except(ValueError):
            print "{p}: error: argument number: invalid int value: {u}".format(
                p=sys.argv[0],
                u=uinput
                )                 
            sys.exit(1)
    return [verbosity,uinput]

def main():
    verbosity,uninput = manage_cli_args()
        

if __name__ == '__main__':
    main()
