#program to print sum of n numbers

n=int(input("Enter a number:"))

i=n-1
while (n>=0):
    sum=n+i
    i-=1
print(sum)