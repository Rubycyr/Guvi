A=raw_input()
A=A.split()
for num in range(int(A[0])+1,int(A[1])):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
