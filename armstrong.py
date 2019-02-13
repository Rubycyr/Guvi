user=raw_input()
user=int(user)
sum=0
temp=user
while user>0:
    rem=user%10
    sum=sum+(rem**3)
    user=user/10
if sum==temp:
    print"yes"
else:
    print'no'
