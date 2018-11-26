#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   change_PAL_value.py                                      #
#    Purpose:        Process the data from the shell script and compute       #
#                    the new PAL value and put it into weica.                 #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

sleeping=float(sys.argv[2])
work=sys.argv[3]
free=sys.argv[4]

work=work.split(":")
free=free.split(":")

import weica

c=weica.consumption("q")

f = open(path+"/data/PAL_values.txt", "r")
header1 = f.readline()
PAL_values={}
for line in f:
    line = line.strip()
    columns = line.split()
    activity = columns[0]
    PAL = float(columns[1])
    PAL_values[activity]=PAL

eff_PAL="{0:.2f}".format((sleeping/24)*PAL_values["sleeping"]+(float(work[0])/24)*PAL_values[work[1]]+(float(free[0])/24)*PAL_values[free[1]])

print("Changing PAL value to " + eff_PAL)

c.change_user_data("PAL", float(eff_PAL))
