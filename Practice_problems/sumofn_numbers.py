#program to print sum of n numbers

n=int(input("Enter a number:"))

i=n

while(n>=1):
    i=i+(n-1)
    n-=1

print(i)