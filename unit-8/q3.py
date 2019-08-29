from itertools import combinations
def combsort(str1,k):
  print ("\nAll possible combinations, up to size k, of the string in lexicographic sorted order:")
  fo.write("\nAll possible combinations, up to size k, of the string in lexicographic sorted order:\n")
  for ch in str1:
    print (ch)
    fo.write(ch+"\n")
  tuplist=list(combinations(str1,k))
  for tup in tuplist:
    res=''.join(tup)
    print (res)
    fo.write(res+"\n")


try:
	fo=open("opfileq3.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	string=raw_input("\nEnter string: ")
	fo.write("String: "+str(string))
	str1=sorted(string)
	k=int(input("Enter size k for the string: "))
	combsort(str1,k)
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting all possible combinations, up to size k, of the string in lexicographic sorted order is executed successfully!")

	
finally:
	print ("\nFinished.\n")
