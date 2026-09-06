#block of code which performs a specific task is called a function

def func1(a,b): #def is a keyword used to define the functions, the () and : are necessary
    # the (a,b) are the values that func1 takes as a function

    sum=a+b
    print(sum) #but this will not return any output
    return sum #this is necessary if any output is expected

func1 (1, 99) #this is a function call **** (semicolon isn't used here)
#the values that are input will be put in the function

func1 (1,1)

sum=func1 (1,-1) #this way can be used if return sum isnt used while defining the function
print(sum)

"""0 IS BEING PRINTED TWO TIMES SINCE func1 (1,-1) prints it once, and print(sum) prints it again"""

def printf():
    print("hello")

printf()