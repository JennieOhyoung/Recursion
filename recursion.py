l = ["a", "b", "c", "d"]
i = [3,6,2,7]
n = 7
s1 = "racecar"

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Multiply all the elements in a list
def multiply_list(l):
    if l == []:
        return 1
    return l[0] * multiply_list(l[1:]) 

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    # new_list = []
    if l == []:
        return []
    # new_list.append(l.pop())
    return [l.pop()] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# Finds the value i in the list l.... RECURSIVELY. Return i if exists, none if dne
def find(l, i):
    if l == []:
        return "Not here."
    elif l[0] == i:
        return i

    return find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    
    if some_string == "":
        # return "It is a palindrome!"
        return True
    elif len(some_string) == 1:
        # return "It is a palindrome!"
        return True

    return some_string[0] == some_string[-1] and palindrome(some_string[1:-1])

    # elif some_string[0] == some_string[-1]:
    #     return palindrome(some_string[1:-1])
    # else:
    #     return "It is NOT a palindrome."

# Given the width and height of a sheet of paper, and the number of times to fold it
# return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    elif width > height:
        return fold_paper(width/2.0, height, folds - 1)
    else:
        return fold_paper(width, height/2.0, folds - 1)
 
# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == target:
        return n
    print n
    return count_up(target, n + 1)



print factorial(n)
print multiply_list(i)
print count_list(l)
print sum_list(i)
print reverse(l)
print fibonacci(n)
print find(l,"c")
print palindrome(s1)
print fold_paper(8,12,3)
print count_up(10, 0)