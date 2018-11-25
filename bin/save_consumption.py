#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

date=sys.argv[2]

c=weica.consumption("q")
c.compute_consumption("q")

if date!="empty":
    c.save_consumption(date)
else:
    c.save_consumption()
