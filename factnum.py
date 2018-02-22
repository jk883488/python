
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
if num > 20:   
   print("Sorry, you reached the limit")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
