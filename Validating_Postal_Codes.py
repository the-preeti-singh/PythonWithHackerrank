import re
P = raw_input()
print len(re.findall(r'(?=(\d)\d\1)',P)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',P))
