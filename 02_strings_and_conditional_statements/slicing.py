# str=[starting_index:ending_index] , ending index is not included in output

string="Batman"

ch=string[0:3]

print(ch)

ch=string[:3] #is the same as [0:3]
print(ch)

ch=string[0:] #is the same as [3:len(string)]
print(ch)
