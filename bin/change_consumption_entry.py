#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   change_consumption_entry.py                              #
#    Purpose:        Process the data from the shell script and change the    #
#                    corresponding consumption entry.                         #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")

entry=sys.argv[2].split(":")
mode=sys.argv[3]

c.change_consumption_entry(entry[0], float(entry[1]), mode)
c.compute_consumption("l")
