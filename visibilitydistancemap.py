#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (sid, visdist, qual) = (val[4:10], val[78:84], val[84:85])
  if (visdist != "999999" and re.match("[01459]", qual)):
    print "%s\t%s" % (sid, visdist)
