#!/usr/bin/env python3
import sys

path=sys.argv[1]
sys.path.insert(0, path)

import weica

c=weica.consumption("q")

show=int(sys.argv[2])

c.plot_consumption(show)
