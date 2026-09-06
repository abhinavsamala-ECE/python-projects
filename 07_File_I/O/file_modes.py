"""Small examples of Python file modes.

Each example uses a different file mode.  The comments explain what happens
in very simple words.
"""


# "w" means write.  It makes a new file and puts words inside it.
# If the file already has words, "w" cleans them away first.
with open("write.txt", "w") as file:
    file.write("Hello!\n")


# "r" means read.  It lets us look at words that are already in a file.
# The file must already exist.
with open("write.txt", "r") as file:
    words = file.read()
    print("Read mode:", words)


# "a" means add.  It puts new words at the end and keeps the old words safe.
with open("write.txt", "a") as file:
    file.write("This is an added line.\n")


# "x" means create.  It makes a brand-new file only.
# It gives an error if the file is already there, so it cannot overwrite it.
try:
    with open("new_file.txt", "x") as file:
        file.write("I am a new file!\n")
except FileExistsError:
    print("new_file.txt already exists.")


# "r+" means read and write.  We can look at the file and then change it.
# The old words are not automatically erased.
with open("read_write.txt", "w") as file:
    file.write("Read and write\n")

with open("read_write.txt", "r+") as file:
    print("r+ mode:", file.read())
    file.write("A new line\n")


# "w+" means write and read.  It cleans the file first, then lets us do both.
with open("write_read.txt", "w+") as file:
    file.write("I can write and read!\n")
    file.seek(0)  # Go back to the beginning to read the words.
    print("w+ mode:", file.read())


# "a+" means add and read.  Old words stay, and new words go at the end.
with open("add_read.txt", "a+") as file:
    file.write("One more line\n")
    file.seek(0)  # Go back to the beginning to read everything.
    print("a+ mode:", file.read())


# "rb" means read bytes.  Bytes are tiny computer pieces used for pictures
# and other files that are not ordinary text.
with open("write.txt", "rb") as file:
    some_bytes = file.read(5)
    print("rb mode:", some_bytes)


# "wb" means write bytes.  Here we make a tiny binary file.
with open("tiny.bin", "wb") as file:
    file.write(b"ABC")