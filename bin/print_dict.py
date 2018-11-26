#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   print_dict.py                                            #
#    Purpose:        Process data from the shell script and print the         #
#                    corresponding dictionary entries.                        #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

li=[]
if len(sys.argv)==3:
    li=sys.argv[2].split(";")
        
c=weica.consumption("q")

if len(li)!=0:
    c.print_dict(li)
else:
    c.print_dict()
