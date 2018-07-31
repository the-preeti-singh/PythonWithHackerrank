import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    child_depths = [ depth(child,level+1)   for child in elem ]
    if not child_depths:
        return level + 1
    else:
        fattest_kid = max(child_depths)
        if level == -1:
            maxdepth = fattest_kid
        else:
            return fattest_kid
          
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
