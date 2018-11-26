#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   compute_consumption.py                                   #
#    Purpose:        Compute the current calory consumption.                  #
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
c.compute_consumption("l")
