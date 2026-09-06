n=int(input("Enter a number:"))

i=n

while(n>1):
    i=i*(n-1)
    n=n-1

print("The factorial of n is",i)