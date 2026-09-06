set1={1,2,3,4,5}
set2={6,7,8,9,10}

set1.add(10) #adds an element
print(set1)

set1.remove(3) #removes an element
print(set1)

x= set1.pop() #removes a random value
print(x)

print(set1.union(set2)) #combines the values of both sets and makes a new set

print(set1.intersection(set2)) #combines the common values and makes a new set

"""set1.clear() #removes all the elements in a set
print(set1)"""

"""SET is mutable(changeable) ELEMENT inside a set is IMMUTABLE"""