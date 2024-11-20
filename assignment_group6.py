# Create a function is_palindrome(word) that returns True if
# a given word is a palindrome (reads the same backward) and False otherwise.

def palindrome(string):
    """
    :param string:
    :return: True if the string is a palindrome, false if not

    pseudocode:

    from the right to the center is same as from left
    to the center
    0 == -1
    1 == -2

    for example "noon" 0==-1 , 1 == -2
    0, 1, -2, -1

    12x-1
    0 1 2 -3 -2 -1
    half = len // 2
    len - 1
    8

    example : madam
    len = 6
    half = 3
    0 1 2
    i = 0
    while i <= half
        - (i + 1)
        if 0 == -1
            continue
        else
            return false
    return true
    """
    string_length = len(string)
    half_of_length = int(string_length / 2)
    i = 0
    while i <= half_of_length:
        if string[i] == string[- (i + 1)]:
            i += 1
            continue
        else:
            return False
    return True
print(palindrome("noon"))
print(palindrome("racecar"))
print(palindrome("table"))
print(palindrome("eat"))

# Write a function reverse_string(s) that takes a string s and returns the reversed string
def reverse_string(string):
    """reverses a string"""
    reversed_string = ''
    i = 1

    while i <= len(string):
        reversed_string += string[-i]
        i += 1

    return reversed_string
print(reverse_string("ruby"))
print(reverse_string("juice"))
print(reverse_string("racecar"))

# Write a function fibonacci(n) that generates a list containing the first n numbers in the Fibonacci sequence.
def fib(n):
    """

    :param n:
    :return: fib of first n numbers

    0, 1, 1, 2, 3, 5, 8, 13
    a, b,
       a, b,
          a, b,
             a, b
                a, b,
    a = 0
    b = 1
    print(a, b)
    for i in range(n):
        temp = a
        print  (a + b)
        a = b
        b = b + temp
    """
    a = 0
    b = 1
    print(a, b, end=",")
    for i in range(n - 2):
        temp = a
        print(a + b, end=",")
        a = b
        b = b + temp
n = 10
fib(n)