#program to find x in the list [1,4,9,16,25,36,49,64,81,100] using a loop

list=[1,4,9,16,25,36,49,64,81,100]

c=int(input("Enter a number to find in the list:"))

while c in list:
    print("Found")
    break #break is used to terminate the loop when the condition is met
else:
    print("Not Found")