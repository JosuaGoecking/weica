#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   print_consumption.py                                     #
#    Purpose:        Process data from the shell script and print the         #
#                    consumption.                                             #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")
c.print_consumption()
