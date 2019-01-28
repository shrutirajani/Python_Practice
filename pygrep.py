import sys
import re

myre = re.compile(sys.argv[1])

for line in sys.stdin:
    line = line.strip()
    if myre.search(line):
        print(line)
