
import re

s = input()
k = input()
index = 0

if re.search(k, s):
    while index+len(k) < len(s):
        m = re.search(k, s[index:]) #begins search with new index
        
        print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
        index += m.start() + 1 #assign new index by +1 
else:
    print((-1, -1))
