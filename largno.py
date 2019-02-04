A=int(input())
B=int(input())
C=int(input())
if (A>=B) and (A>=C):
	largest=A
elif (B>=A) and (B>=C):
	largest=B
else:
	largest=C
print (largest)
