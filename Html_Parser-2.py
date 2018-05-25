import re

if __name__ == '__main__':
    n = int(raw_input().rstrip())
    while (n > 0):
        n-=1
        s = str(raw_input())
        if re.findall('<.*>(.*)</.*>',s):  #look for data tag in each line
            m = re.findall('<.*>(.*)</.*>',s)
            print ">>> Data"
            print m[0]
        elif re.findall('<!--(.*)-->',s): # look for single-line comment in each line
            m = re.findall('<!--(.*)-->',s)
            print ">>> Single-line Comment"
            print m[0]
        elif re.findall('<(.*)/>',s):
            continue
        else:       
            print ">>> Multi-line Comment"
            s = re.sub(r'<!--','',s) # strip start of comment tag
            print s
            s = str(raw_input())
            n-=1
            while not (re.findall(r'-->',s)): #while end tag not found
                print s
                s = str(raw_input()) #scan new line
                n-=1 #decrement lines left
            s = re.sub(r'-->','',s) # get rid of end of comment tag
            print s     
