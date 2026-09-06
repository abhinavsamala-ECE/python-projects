def rec1(n):
    i=n
    while(n>0):  #the while condition itself terminates the recursion
        i=i+(n-1)
        n-=1  
    print(i)
    return i


rec1(10)