#program to print elements in a list using a recursive function

def print_list(lst, i):
    if i == len(lst):
        return
    print(lst[i])
    print_list(lst, i + 1)

list = [10, 20, 30, 40]
print_list(list, 0)