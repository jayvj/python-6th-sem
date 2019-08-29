from itertools import permutations
def permsort(str1,k):
  print ("\nAll possible permutations of size k of the string in lexicographic sorted order:")
  fo.write("\nAll possible permutations of size k of the string in lexicographic sorted order:\n")
  perm=permutations(str1,k)
  for i in list(perm):
    res=''.join(i)
    print (res)
    fo.write(res+"\n")

	
try:
	fo=open("opfileq2.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	string=raw_input("\nEnter string: ")
	fo.write("String: "+str(string))
	str1=sorted(string)
	k=int(input("Enter size k for the string: "))
	permsort(str1,k)
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting all possible permutations of size k of the string in lexicographic sorted order is executed successfully!")

	
finally:
	print ("\nFinished.\n")
