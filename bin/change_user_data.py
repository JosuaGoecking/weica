#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   change_user_data.py                                      #
#    Purpose:        Process the data from the shell script and change the    #
#                    corresponding user data entries.                         #
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

ch=sys.argv[2]

changes=ch.split(";")

d={}
for i in changes:
    i=i.split(":")
    d[i[0]]=i[1]

for key in d:
    if key=="weight" or key=="abdomen" or key=="height" or key=="neck":
        d[key]=int(d[key])
    if key=="PAL":
        d[key]=float(d[key])
    c.change_user_data(key, d[key])

