#!/usr/bin/env python3
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
