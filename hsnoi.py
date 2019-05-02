<<<<<<< HEAD
count=0
def hanoi(n,src,dst,mid):
	global count
	if n==1:
		print("{}:{}->{}".format(1,src,dst))
		count+=1
	else:
		hanoi(n-1,src,mid,dst)
		print("{}:{}->{}".format(n,src,dst))
		count+=1
		hanoi(n-1,mid,dst,src)
hanoi(3,"A","C","B")
=======
count=0
def hanoi(n,src,dst,mid):
	global count
	if n==1:
		print("{}:{}->{}".format(1,src,dst))
		count+=1
	else:
		hanoi(n-1,src,mid,dst)
		print("{}:{}->{}".format(n,src,dst))
		count+=1
		hanoi(n-1,mid,dst,src)
hanoi(3,"A","C","B")
>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
print(count)