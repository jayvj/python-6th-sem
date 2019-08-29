from itertools import groupby

S="21133211"
print ("\nstring S: ")
print (S)
listres=[]
groups = groupby(S)
for label,group in groups:
    result=(sum(1 for _ in group),int(label))
    listres.append(result)
print ("\nOutput:")
print (listres)
print ("\n")