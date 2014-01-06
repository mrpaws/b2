b2
==

translates binary and decimal (base 2 &lt;=> base 10)



Summary:

A useful learning project.

Under development but functionally sound, this program will convert base 2 to base 10 and vice versa.  Verbose output does not work yet but ideally will show the math involved in the conversion process.

Features:

-  reusable code
-  tries to determine what you're passing it
-  accepts input from stdin (via a pipe or interactively) and cli

Use cases: 

binary => decimal
$ python b2.py 100010101101
2221

decimal => binary, with input from a pipe
$ echo "50000120013132" | python b2.py 
1011010111100110001111011001000110000101001100

TODO:

-  Add verbose output
-  Add options for explicilty specifying translation operation
-  Add hexadecimal translation
-  clean up code/comments
-  modularize
-  narrow down module imports
-  possibly ditch argparse

Development Notes:

This is another learning project with some good takeaways:

* If you're looking to reuse or improve the translation operations, check out private methods of Translator: _translate_binary, _translate_decimal

-  first time i actually bothered to try and properly handle CLI arguments in Python and disappointed with argparse at first glance.  started with getopt, but documentation really pushed toward using argparse.  argparse reduces code, simplifies and streamlines argument handling except for one big thing:  there does not seem to be a straight forward way to accept a positional argument from different possible streams.  am able work around this until skill/improvements with argparse allow me to take the primary chunk of information either from a pipe if data is sent, on the command line if it is present and otherwise accept data interactively from stdin. could just be something i'm missing but this is really easy for setting up custom argument parsers but cumbersome to integrate.  ultimately may just override some methods to integrate functionality










