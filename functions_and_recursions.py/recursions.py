#when a function calls itself repeatedly (loop but for functions)

def show(n):
    if (n==0):
        return  #this if block terminates the recursion
    print(n)
    show(n-1)

show(5)
