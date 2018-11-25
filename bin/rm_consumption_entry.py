#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")

ent=sys.argv[2]

c.rm_consumption_entry(ent)
c.compute_consumption("l")
