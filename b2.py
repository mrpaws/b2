#!/usr/bin/env python
'''
  b2.py - translate decimal and binary
  Author:
      mrpaws
  Project Repo:
      https://github.com/mrpaws/b2
'''

import sys
import argparse
from types import IntType

class B2Exception(Exception):
    '''pass generic b2 module exceptions
    '''
    pass

class Translator:
    '''b2 translator object'''
    def __init__(self, value):    
        self.value = value
        #assert(type(self.value)) is IntType, "{m}{v}".format(
            #m="value is not an number: ",
            #v=value
            #)
        self.str_value = self._conv_str()
        self.base = self._identify_base()
        self.translation = None

    def _conv_str(self):
        '''private method to convert int to string 
           for digit manipulation for bitwise calculations
        '''
        try: 
            str_value = str(self.value)
        except(ValueError):
            error = "Unable to manipulate value as a string: ({v}).".format(
                v=value
                )
            raise B2Exception(error)
            return False
        return str_value

    def _identify_base(self):
        '''private method to identify base of input (10 or 2)
        '''
        base = 2
        '''try to guess whether input is a decimal of binary
           ideally user should specify
        '''
        for c in self.str_value:
            if int(c) > 1:
                base = 10
                break
        return base
    
    def _translate_binary(self):
        '''private method to translate a binary to a decimal
        '''
        product = 0
        i = 0
        numlen = len(self.str_value)
        exp = numlen-1 
        while (i < numlen):
            bit = int(self.str_value[i])
            bit_decval = bit*self.base**exp
            product = product + bit_decval
            i=i+1
            exp = exp - 1
        return str(product)

    def _translate_decimal(self):
        '''private method to translate a decimal to a binary
        '''
        c_value = self.value
        bits = []
        while (c_value != 0): 
            bits.append(c_value % 2)
            c_value = c_value / 2
        bits.reverse()
        return ''.join(map(str, bits))

    def translate(self):
        '''perform translations and return the result to the user'''
        if self.base == 2:
            self.translation = self._translate_binary()
        elif self.base == 10:
            self.translation = self._translate_decimal()
        return self.translation

        

def manage_cli_args():
    '''parse command line arguments/stdin
    '''
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

    ''' Python documentation pushes argparse but this
        hack would not be necessary with getopt
    '''
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
    '''MAIN Main main
    '''
    verbosity,uinput = manage_cli_args()
    try:
        translation = Translator(uinput)
        value = translation.translate()
    except(B2Exception) as errormsg:
        print errormsg
        sys.exit(2)
    print value

if __name__ == '__main__':
    main()
