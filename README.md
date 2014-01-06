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
-  -  possibly ditch argparse




