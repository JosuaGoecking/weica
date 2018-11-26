#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   rm_recipe_entry.py                                       #
#    Purpose:        Process data from the shell script and remove the        #
#                    corresponding recipe entry.                              #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

ent=sys.argv[2].split(":")

c=weica.consumption("q")
c.rm_recipe_entry(ent[0], ent[1])
