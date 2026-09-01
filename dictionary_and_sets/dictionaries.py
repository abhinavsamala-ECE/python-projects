# A dictionary is like a notebook where you write down questions and answers!
# For example: question="What is your name?" answer="Alice"
# You look up the question to find the answer!

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(my_dict)           # Show the whole notebook
print(my_dict['name'])   # What is the name? Answer: Alice
print(my_dict['age'])    # What is the age? Answer: 25

my_dict['age'] = 26      # Change the age answer to 26
print(my_dict)           # Show the updated notebook

del my_dict['city']      # Erase the city from the notebook
print(my_dict)           # Show what's left

print('name' in my_dict) # Is "name" in our notebook? True!
print('city' in my_dict) # Is "city" in our notebook? False! (we erased it)

print(my_dict.keys())    # Show all the questions
print(my_dict.values())  # Show all the answers
print(my_dict.items())   # Show all questions and answers together

del my_dict['Alice'] #type: ignore this will raise a KeyError because 'Alice' is not a key in the dictionary
#only keys can be deleted, not values.
