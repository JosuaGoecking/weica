#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

ent=sys.argv[2].split(":")

c=weica.consumption("q")
c.rm_recipe_entry(ent[0], ent[1])
