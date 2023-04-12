import sys
print(sys.path)

import re
text = 'mi numero de telefono es 1221315 my pais 57 mi numero suerte 3'

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections

numbers = [1,1,1,1,3,3,4,5,5,6,66]

counter = collections.Counter(numbers)
print(counter)