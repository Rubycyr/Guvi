Num = int(input("Please Enter the Num: "))

if (( Num%400 == 0)or (( Num%4 == 0 ) and ( Num%100 != 0))):
    print("%d is a Leap Year" %Num)
else:
    print("%d is Not the Leap Year" %Num)
