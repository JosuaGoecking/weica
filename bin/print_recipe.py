#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   print_recipe.py                                          #
#    Purpose:        Process data from the shell script and print the         #
#                    corresponding recipe.                                    #
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

name=sys.argv[2]

c.print_recipe(name)
