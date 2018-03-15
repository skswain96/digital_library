import os
from urllib.parse import urlparse


file = open('queue.txt','r')
output = open('output.txt','w')
for line in file:
    line = file.readline()
    parse_obj = urlparse(line)
    if parse_obj.netloc[0] == 'f':
        output.write(line)
    else:
        pass



file.close()
