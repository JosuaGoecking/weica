#!/usr/bin/env python3                                                                                                                                                             
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

m=sys.argv[2]
d=sys.argv[3]

meta={}
data={}

m1=m.split(";")
d1=d.split(";")

for i in m1:
    i=i.split(":")
    meta[i[0]]=i[1]
for i in d1:
    i=i.split(":")
    data[i[1]]=[float(i[0]), "d.u."]

meta["Gewürze"]=meta["Gewürze"].replace("_", " ")
meta["Zubereitung"]=meta["Zubereitung"].replace("_", " ")
meta["Zubereitung"]=meta["Zubereitung"].replace("§", "\n")
meta["Portionen"]=int(meta["Portionen"])

d={"meta":meta, "Zutaten":data}

c=weica.consumption("q")
c.add_recipe(d)
c.print_recipe(d["meta"]["Name"])
