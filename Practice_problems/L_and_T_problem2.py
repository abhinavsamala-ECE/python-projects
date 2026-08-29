#program to check if a list contains a palindrome of elements

a=[0,"hello",0]
b=[]

b=list(reversed(a)) #list() turns the reversed(a) into a list

print("Yup it's a palindrome.") if(a==b) else(print("Nah not a palindrome."))
