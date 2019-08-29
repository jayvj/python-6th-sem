class reverse_iter:
  def __init__(self,arrlist):
    self.data=arrlist
    self.pos=len(self.data)
  def __iter__(self):
    return self
  def next(self):
    if self.pos==0:
      raise StopIteration
    self.pos=self.pos-1
    return self.data[self.pos]


try:
  fo=open("opfileq9.txt","r+")
  fo.seek(0,0)
  fo.truncate()
  list1=[]
  num=int(input("\nEnter the no of elements for list1: "))
  fo.write("List1: ")
  for i in range(num):
    ele=raw_input("Enter element"+str(i+1)+": ")
    fo.write(str(ele)+" ")
    list1.append(ele)
  print (list1)
  print ("\nIterating list from the reverse direction:")
  fo.write("\nIterating list from the reverse direction: ")
  for ele in reverse_iter(list1):
    print (ele)
    fo.write(ele+str(" "))


except IOError:
  print ("\nAn error occured trying to read the file.")
except:
  print ("\nAn error occured.")


else:
  print ("\nAn iterator class reverse_iter that takes a list and iterates it from the reverse direction is executed successfully!")

  
finally:
  print ("\nFinished.\n")