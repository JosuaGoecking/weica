#!/usr/bin/env python3

###############################################################################
#                                                                             #
#    Program name:   add_consumption_script.py                                #
#    Purpose:        Process data from the shell script and add it to the     #
#                    consumption in weica.                                    #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

rec=sys.argv[2] # recipes
add=sys.argv[3] # add directly to consumptio
rm=int(sys.argv[4]) # remove previous consumption?

c=weica.consumption("q")

# Remove previous consumption if wanted
if rm == 1:
    c.rm_consumption_entry("all")

# Get the recipe data and add it the consumption
if rec!="empty":
    rec=rec.split(";")
    for entry in rec:
        entry=entry.split(":")
        name=entry[0]
        entry.pop(0)
        for i in range(0, len(entry), 2):
            entry[i]=float(entry[i])
        c.add_recipe_to_consumption(name, entry)

# Get the data of individual add to the consumption and add them
if add!="empty":
    add=add.split(":")
    for i in range(0, len(add), 2):
        add[i]=float(add[i])
    c.add_consumption(add)

c.compute_consumption("l")
