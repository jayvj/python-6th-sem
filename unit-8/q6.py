from itertools import combinations

def probability(letterlist):
  c=0
  for i in letterlist:
    i=list(i)
    for j in i:
      if j=='a':
        c+=1
        break
  length=len(letterlist)
  fo.write("\nCombinations of the list: ")
  for i in letterlist:
    fo.write(str(i)+" ")
  res=float(c)/float(length)
  print ("\nProbability that at least one of the K indices selected will contain the letter:'a': %.4f\n"%res)
  fo.write("\nProbability that at least one of the K indices selected will contain the letter:'a': "+str(round(res,4)))


fo=open("opfileq6.txt","r+")
fo.seek(0,0)
fo.truncate()
fo.write("List: ")
N=int(input("\nEnter the length of the list: "))
letterlist=[]
for i in range(N):
  letter=raw_input("Enter letter"+str(i+1)+": ")
  fo.write(letter+" ")
  letterlist.append(letter)
print ("\nList:")
print (letterlist)
K=int(input("\nEnter the number of indices to be selected:"))
letterlist=list(combinations(letterlist,K))
print ("\nCombinations of the above list:")
print (letterlist)
probability(letterlist)
