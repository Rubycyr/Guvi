A=int(raw_input())
if(A>1):
	for i in range(2,A):
		if(A%i)==0:
			print 'no'
			break
	else:
		print 'yes'
else:
	print 'no'
