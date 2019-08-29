from itertools import *

def izipfunc(list1,list2):
  print ("\nizip function:")
  fo.write("\n\nizip function:")
  print ("Position, list1:element, list2:element:")
  fo.write("\nPosition, list1:element, list2:element:\n")
  for i,a,b in izip(count(),list1,list2):
    print i,a,b 
    fo.write(str(i)+" "+str(a)+" "+str(b)+"\n")


try:
  fo=open("opfileq8.txt","r+")
  fo.seek(0,0)
  fo.truncate()
  list1=[]
  list2=[]
  num=int(input("\nEnter the no of elements for list1 and list2: "))
  print ("\nList1:")
  fo.write("List1: ")
  for i in range(num):
    ele=raw_input("Enter element"+str(i+1)+": ")
    fo.write(str(ele)+" ")
    list1.append(ele)
  print (list1)
  print ("\nList2:")
  fo.write("\nList2: ")
  for i in range(num):
    ele=raw_input("Enter element"+str(i+1)+": ")
    fo.write(str(ele)+" ")
    list2.append(ele)
  print (list2)
  izipfunc(list1,list2)


except IOError:
  print ("\nAn error occured trying to read the file.")
except:
  print ("\nAn error occured.")


else:
  print ("\nImplementing a function izip that works like itertools.izip is executed successfully!")

  
finally:
  print ("\nFinished.\n")