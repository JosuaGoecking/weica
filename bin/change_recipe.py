#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")

name=sys.argv[2]
ent=sys.argv[3]
prep=sys.argv[4]

if ent!="empty":
    ent=ent.split(";")
    li=[]
    for entry in ent:
        entry=entry.split(":")
        li.append(float(entry[0]))
        li.append(entry[1])
    c.change_recipe(name, li)

if prep!="empty":
    prep=prep.replace("_", " ")
    prep=prep.replace("§", "\n")
    c.change_recipe(name, prep)
