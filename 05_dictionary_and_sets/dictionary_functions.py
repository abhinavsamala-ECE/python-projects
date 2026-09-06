#dictionary functions

# A dictionary is like a magic box where you store things with name tags!
# Example: { "name": "Tommy", "age": 5 } - "name" and "age" are the name tags, and "Tommy" and 5 are the things inside

mydict = {}

# keys() - Shows all the name tags in the box
mydict.keys()  # Like saying "show me all the labels!"

# values() - Shows all the things inside the box (not the name tags)
mydict.values()  # Like saying "what's actually inside?"

# items() - Shows both the name tags AND the things inside as pairs (like two friends holding hands!)
mydict.items()  # Returns (name_tag, thing) pairs as tuples
""" pairs[0] will show the 1st (key,value) pair"""

# get() - Safely ask "is there something with this name tag?" and get it if it exists
mydict.get("key")  # Safe way to look up - won't break if name tag doesn't exist

# clear() - Empty the whole magic box! Remove everything!
mydict.clear()  # Whoosh! Everything is gone!

# pop() - Take out one specific thing using its name tag and remove it from the box
mydict.pop("key")  # "key" is gone now!

# popitem() - Take out the last thing you put in (like taking the top toy from a toy pile)
mydict.popitem()  # Removes the newest thing

# update() - Add new things to your box OR change things that are already there
mydict.update({"new_key": "new_value"})  # Add new stuff or update old stuff!

# copy() - Make a copy of the whole box (like making a photocopy of your toy list)
mydict.copy()  # Creates a new copy, original stays the same!

# setdefault() - Look for a name tag, if it exists show what's there, if not add it with a default thing
mydict.setdefault("key", "default_value")  # "I want this thing, or use this if not there!"

# fromkeys() - Create a brand new box with specific name tags, all with the same thing inside
dict.fromkeys(["key1", "key2"], "same_value")  # All have the same value!

# len() - Count how many name tags (things) you have in your box
len(mydict)  # "How many toys do I have?"

# in operator - Check if a specific name tag exists in your box (like checking "do I have a toy called teddy?")
"key" in mydict  # True if the name tag exists, False if not

# del - Remove one specific thing from your box by its name tag (delete from the box!)
del mydict["key"]  # "key" and its thing are gone forever!
