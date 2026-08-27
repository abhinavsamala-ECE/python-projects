"""
<var> = (false_val, true_val)[condition]

if the [condition] is true, then the value of <var> will be true_val, else it will be false_val"""

age= int(input("Enter your age: "))
vote = ("not eligible","eligible")[age>=18]
print(vote)