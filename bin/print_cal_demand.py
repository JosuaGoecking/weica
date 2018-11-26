#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   print_cal_demand.py                                      #
#    Purpose:        Process the data from the shell script and print the     #
#                    calory demand.                                           #
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
c.print_cal_demand()
