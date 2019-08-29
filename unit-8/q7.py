from itertools import count

def my_enumerate(values):
  return list(zip(count(),values))


try:
  fo=open("opfileq7.txt","r+")
  fo.seek(0,0)
  fo.truncate()
  num=int(input("\nEnter the no of values: "))
  fo.write("Values: ")
  values=[]
  for i in range(num):
    val=int(input("Enter num"+str(i+1)+": "))
    values.append(val)
  print ("\nValues: ")
  print (values)
  for i in values:
    fo.write(str(i)+" ")
  res=my_enumerate(values)
  print ("\nmy_enumerate:")
  print (res)
  fo.write("\nmy_enumerate:")
  for i in res:
    fo.write(str(i))
  

except IOError:
  print ("\nAn error occured trying to read the file.")
except:
  print ("\nAn error occured.")


else:
  print ("\nmy_enumerate that works like enumerate is executed successfully!")

  
finally:
  print ("\nFinished.\n")