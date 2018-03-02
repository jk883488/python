def odd(i,j):
	if((j%2)==0):
		if(abs(j-i)==1 or abs(j-i)==0):
			print("no odd numbers")
		j=j+1
		while(j!=i and j!=(i+1)):
			print(j)
			j=j+2
	else:
		if(abs(i-j)==2 or abs(i-j)==1):
			print("no odd numbers")
		j=j+2
		while(j!=i and j!=(i+1)):
			print(j)
			j=j+2


def raw_input():
  j,i=[int(x) for x in raw_input().split(",")]
  if(j<i):
	  odd(j,i)
			
  elif(j>i):
	  temp=j
	  j=i
	  i=temp
	  odd(j,i)
  else:
	  odd(j,i)
