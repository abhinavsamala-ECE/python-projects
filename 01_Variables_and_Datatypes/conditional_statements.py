#python program to check if a number is positive, negative, even or odd
num=int(input("Enter a number: "))
if num>0: #the : is used to indicate the start of a block of code and is important
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

if num%2==0:
    print("The number is even")   #the space before the print statement is important, it indicates that this line is part of the if block
else:
    print("The number is odd")


"""SINGLE LINE IF ELSE STATEMENT"""

food=input("food:")   #input statement

eat = "yes" if food == "pizza" or food == "shawarma" else "no"  # The first value is used when the condition is true.
print(eat)

"""

***TWO WAYS TO PUT TWO CONDITIONS IN IF STATEMENT:

#way 1: using if food == "pizza" or food == "shawarma":

#way 2: using if food in ["pizza", "shawarma"]
 

 """