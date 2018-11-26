#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   initialize.py                                            #
#    Purpose:        Process the initialization data from the shell script    #
#                    and initialize weica.                                    #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)
user_data = sys.argv[2]

d_user = {}
pairs = user_data.split(";")

for pair in pairs:
    data_pair = pair.split(":")
    d_user[data_pair[0]] = data_pair[1]

d_user["PAL"] = 1.7
print("The physical activity level (PAL) value was set to a default of 1.7. You can update it with your individual PAL value by running 'weica -e PAL'.")

for key in d_user:
    if key=="weight" or key=="abdomen" or key=="height" or key=="neck":
        d_user[key]=int(d_user[key])
    if key=="PAL":
        d_user[key]=float(d_user[key])

import weica

c = weica.consumption(d_user)
