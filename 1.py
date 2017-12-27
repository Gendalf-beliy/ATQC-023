def hello(arg):
    '''
    Function, that takes string as argument and prints "Heelo, %arg%!"
    >>> hello('Vasya')
    'Hello, Vasya!'
    '''
    return 'Hello, {}!'.format(arg)
    

def histogram(num_list):
    '''
    Procedure that takes a list of integers and prints a histogram to the screen.
    Usage time.sleep(s) possible for better visualization
    >>> histogram([4, 9, 7])   
    ****
    *********
    *******
    '''
    import time
    for num in num_list:
        time.sleep(1.5)
        print('*' * num)


def sums(lst):
    '''
    Function sums all the numbers in a list of numbers.
    >>> sums([1, 2, 3, 4])
    10
    '''
    result = 0
    for number in lst:
        result += number
    return result
    

def multiply(lst):
    '''
    Function that multiplies all the numbers in a list of numbers. 
    >>> multiply([1, 2, 3, 4])
    24
    '''
    result = 1
    if 0 in lst:
        return 0
    else:
        for number in lst:
            result *= number
        return result
        

def reverse(string):
    '''
    Function  that computes the reversal of a string.  
    >>> reverse("I am testing") 
    'gnitset ma I'
    '''
    result = ''
    for char in string:
        result = char + result
    return result


def is_palindrome(string):
    '''
    Function that recognizes palindromes (i.e. words that look the same written 
    backwards). 
    >>> is_palindrome("radar")
    True
    '''
    if string == reverse(string):
        return True
    else:
        return False


def caesar_cipher(string, shift):
    ''' Function that takes string and key(number), which returns encrypted string
    >>> caesar_cipher('abc', 1)
    'bcd'
    '''
    encrypted = ''
    return encrypted


def diagonal_reverse(matrix):
    '''
    Function that takes matrix and returns diagonal-reversed one. For example,
    1 2 3         1 4 7
    4 5 6 returns 2 5 8
    7 8 9         3 6 9
    >>> diagonal_reverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = []
            temp.append(matrix[i][j])
        diagonal.append(temp)
    return diagonal


def number_guessing():
    '''
    Function game, that takes 2 int parameters defining the range. 
    Using random.randint(A, B) generate random int from the range. 
    While user input isn't equal that number, print "Try again!". 
    If user guess the number, congratulate him and exit. (use input())
    '''

def is_brackets_balanced(string):
    '''
    Function, which takes a string with N opening brackets ("[") and N closing 
    brackets ("]"), in some arbitrary order. Determine whether the generated 
    string is balanced; that is, whether it consists entirely of pairs of 
    opening/closing brackets (in that order), none of which mis-nest.
    Examples:

    []        OK   ][        NOT OK
    [][]      OK   ][][      NOT OK
    [[][]]    OK   []][[]    NOT OK
    >>> is_brackets_balanced('[]')
    'OK'
    >>> is_brackets_balanced('][')
    'NOT OK'
    >>> is_brackets_balanced('[][]')
    'OK'
    >>> is_brackets_balanced('][][')
    'NOT OK'
    '''

def char_freq(string):
    '''
    Function that takes a string and builds a frequency listing of the 
    characters contained in it. Represent the frequency listing as a Python 
    dictionary. 
    >>> char_freq("abbabcbdbabdbdbabababcbcbab")
    {'a': 7, 'b': 14, 'c': 3, 'd': 3}
    '''
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
    

def dec_to_bin(number):
    '''
    Function that takes decimal integer and outputs its binary representation.
    '''
    return 1


def battle_ship():
    '''
    Write a ship battle game, which is similar to ex.8, except it takes 
    1 integer as an order of matrix, randomly generates index (x, y) and 
    checks user input (2 integers).
    (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
    '''
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()