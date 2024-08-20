#!/usr/bin/env python

import sys

(last_key, vissum, val) = (None, 0, 0)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  if last_key and last_key != key:
    print "%s\t%s" % (last_key, vissum/num)
    (last_key, vissum, num) = (key, int(val), 1)
  else:
    (last_key, vissum, num) = (key, (vissum+int(val)), num+1)

if last_key:
  print "%s\t%s" % (last_key, vissum/num)