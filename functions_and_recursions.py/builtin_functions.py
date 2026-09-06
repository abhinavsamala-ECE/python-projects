"""Small, friendly examples of Python's most commonly used built-in functions."""

# print() shows something on the screen, like talking out loud.
print("Hello!")

# len() counts things, like counting your toys.
print(len("cat"))

# type() tells us what kind of thing something is.
print(type(7))

# int() changes a number into a whole number.
print(int("5"))

# float() changes a number into one that can have a dot.
print(float("2.5"))

# str() changes something into words.
print(str(10))

# bool() says whether something is True or False.
print(bool(1))

# abs() removes the minus sign, so the number is never below zero.
print(abs(-8))

# round() makes a number shorter and neater.
print(round(3.7))

# min() finds the smallest number in a group.
print(min(4, 1, 9))

# max() finds the biggest number in a group.
print(max(4, 1, 9))

# sum() adds all the numbers together.
print(sum([1, 2, 3]))

# sorted() puts things in order, like lining up toys by size.
print(sorted([3, 1, 2]))

# reversed() lets us look at things from the end to the beginning.
print(list(reversed([1, 2, 3])))

# range() makes a counting line of numbers.
print(list(range(1, 4)))

# list() makes a list, which is a box for many things.
print(list("abc"))

# tuple() makes a group of things that should not change.
print(tuple([1, 2, 3]))

# set() keeps only one copy of each thing.
print(set([1, 1, 2]))

# dict() makes a word-and-answer box.
print(dict(name="Mia", age=5))

# zip() joins matching items, like pairing socks.
print(list(zip(["red", "blue"], [1, 2])))

# enumerate() gives each item a number tag.
print(list(enumerate(["apple", "banana"], start=1)))

# all() is True only when every answer is True.
print(all([True, True]))

# any() is True when at least one answer is True.
print(any([False, True]))

# open() opens a file so Python can read or write it.
# This example opens the file safely and then closes it automatically.
with open("builtin_example.txt", "w") as file:
	file.write("Hello from Python!")

# input() asks the person running the program a question.
# It is kept as a comment so this example does not pause unexpectedly.
# favorite_color = input("What is your favorite color? ")

# id() gives an object a special identity number while the program runs.
print(id("hello"))

# help() gives information about Python things.
# help(len)  # Uncomment this to read about len.

# dir() shows the things an object knows how to do.
print("upper" in dir("hello"))

# callable() checks whether something can be used like a function.
print(callable(print))

# isinstance() checks whether something is a certain kind of thing.
print(isinstance(5, int))

# issubclass() checks whether one class is a kind of another class.
print(issubclass(bool, int))

# pow() raises a number to a power, like multiplying it by itself.
print(pow(2, 3))

# divmod() gives both the answer and the leftover after division.
print(divmod(7, 3))

# format() makes a number or word look the way we choose.
print(format(3.14159, ".2f"))
