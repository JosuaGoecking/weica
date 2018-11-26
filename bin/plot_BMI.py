#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   plot_BMI.py                                              #
#    Purpose:        Process data from the shell script and plot the BMI.     #
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

show=int(sys.argv[2])

c.plot_BMI(show)
