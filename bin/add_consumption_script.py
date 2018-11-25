#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

rec=sys.argv[2]
add=sys.argv[3]
rm=int(sys.argv[4])

c=weica.consumption("q")

if rm == 1:
    c.rm_consumption_entry("all")

if rec!="empty":
    rec=rec.split(";")
    for entry in rec:
        entry=entry.split(":")
        name=entry[0]
        entry.pop(0)
        for i in range(0, len(entry), 2):
            entry[i]=float(entry[i])
        c.add_recipe_to_consumption(name, entry)

if add!="empty":
    add=add.split(":")
    for i in range(0, len(add), 2):
        add[i]=float(add[i])
    c.add_consumption(add)

c.compute_consumption("l")
