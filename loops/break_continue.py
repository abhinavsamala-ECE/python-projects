#break:used to terminate the loop
i=1
while i<=5:
    print(i)
    if (i==3):
        break
    i+=1


#continue:it does not run the loop for the condition we specify and continues it from the next, 4 onwards

i=0
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1