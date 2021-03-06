#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   add_dict_entry.py                                        #
#    Purpose:        Process data from the shell script and add the given     #
#                    dict entry.                                              #
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

entry=sys.argv[2]
data=sys.argv[3].split(":")

c.add_dict_entry(entry, float(data[0]), data[1])
