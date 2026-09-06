age = 20
has_id = True

print("Can enter:", age >= 18 and has_id)
print("Free entry:", age < 5 or age >= 60)
print("Does not have an ID:", not has_id)

"""we dont need to write if else statements seperately, we can just write the condition in the print statement itself,
 and it will return True or False"""