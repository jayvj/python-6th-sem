from itertools import combinations_with_replacement
def replcombsort(str1,k):
  print ("\nAll possible size k replacement combinations of the string in lexicographic sorted order:")
  fo.write("\nAll possible size k replacement combinations of the string in lexicographic sorted order:\n")
  tuplist=list(combinations_with_replacement(str1,k))
  for tup in tuplist:
    res=''.join(tup)
    print (res)
    fo.write(res+"\n")



try:
	fo=open("opfileq4.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	string=raw_input("\nEnter string: ")
	fo.write("String: "+str(string))
	str1=sorted(string)
	k=int(input("Enter size k for the string: "))
	replcombsort(str1,k)
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting all possible size k replacement combinations of the string in lexicographic sorted order is executed successfully!")

	
finally:
	print ("\nFinished.\n")
