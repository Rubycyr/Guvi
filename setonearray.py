A=raw_input()
B=raw_input()
A=A.split()
B=B.split()
sum=0
for i in range(int(A[1])):
	sum=sum+int(B[i])
print sum
