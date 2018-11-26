#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   rm_dict_entry.py                                         #
#    Purpose:        Process data from the shell script and remove the        #
#                    corresponding dictionary entry.                          #
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

entry=sys.argv[2]

c.rm_dict_entry(entry)
