#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")
c.compute_consumption("l")
