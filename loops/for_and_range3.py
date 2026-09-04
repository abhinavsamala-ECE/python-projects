#program to print multilication table of a number

"""n=int(input("Enter a number:"))

i=1

for n in range(1,100): #this is wrong cus n becomes 1,2,3... and so on in this line
    if (i<=10):
      print(n*i)
      i+=1
    """

n=int(input("Enter a number:"))

for i in range(1,11):
    print(n*i)
