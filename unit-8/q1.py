import itertools
def cartesianprod(A,B):
	reslist=[]
	print ("\nCartesian product AxB:")
	for tup in itertools.product(A,B):
		reslist.append(tup)
	print (reslist)	
	fo.write("Cartesian product AxB: "+str(reslist))			
		

try:
	fi=open("ipfileq1.txt","r+")
	fo=open("opfileq1.txt","r+")
	A=[1,2,3]
	B=['a','b']
	fi.seek(0,0)
	fi.truncate()
	fo.seek(0,0)
	fo.truncate()
	fi.write("ListA: "+str(A))
	fi.write("\nListB: "+str(B))
	print ("\nlistA:")
	print (A)
	print ("\nlistB:")
	print (B)
	cartesianprod(A,B)
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nComputing Cartesian product AxB is executed successfully!")

	
finally:
	print ("\nFinished.\n")
