nu = int(raw_input())
tep = nu
rev = 0
while tep <> 0:
	rev = (rev * 10) + (tep % 10)
	tep = tep//10
if nu == rev:
	print("yes")
else:
	print("no")
