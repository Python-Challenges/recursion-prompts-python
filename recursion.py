
# Solve the following prompts using recursion.

# 1. Calculate the factorial of a number. The factorial of a non-negative integer n,
# denoted by n!, is the product of all positive integers less than or equal to n.
# Example: 5! = 5 x 4 x 3 x 2 x 1 = 120
# factorial(5) => 120
def factorial(n):
    pass
# 2. Compute the sum of an array of integers.
# sum([1,2,3,4,5,6]) => 21


def sum_(array):
    pass

# 3. Sum all numbers in an array containing nested arrays.
# arraySum([1,[2,3],[[4]],5]) => 15


def arraySum(array):
    pass

# 4. Check if a number is even.


def isEven(n):
    pass

# 5. Sum all integers below a given integer.
# sumBelow(10) => 45
# sumBelow(7) => 21


def sumBelow(n):
    pass

# 6. Get the integers within a range (x, y).
# range(2,9) => [3,4,5,6,7,8]


def range_(x, y):
    pass

# 7. Compute the exponent of a number.
# The exponent of a number says how many times the base number is used as a factor.
# 8^2 = 8 x 8 = 64. Here, 8 is the base and 2 is the exponent.
# exponent(4,3) => 64
# https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/computing-powers-of-a-number


def exponent(base, exp):
    pass

# 8. Determine if a number is a power of two.
# powerOfTwo(1) => true
# powerOfTwo(16) => true
# powerOfTwo(10) => false


def powerOfTwo(n):
    pass

# 9. Write a function that reverses a string.


def reverse(string):
    pass

# 10. Write a function that determines if a string is a palindrome.


def palindrome(string):
    pass

# 11. Write a function that returns the remainder of x divided by y without using the
# modulo (%) operator.
# modulo(5,2) # 1
# modulo(17,5) # 2
# modulo(22,6) # 4


def modulo(x, y):
    pass

# 12. Write a function that multiplies two numbers without using the * operator or
# Math methods.


def multiply(x, y):
    pass

# 13. Write a function that divides two numbers without using the / operator or
# Math methods to arrive at an approximate quotient (ignore decimal endings).


def divide(x, y):
    pass

# 14. Find the greatest common divisor (gcd) of two positive numbers. The GCD of two
# integers is the greatest integer that divides both x and y with no remainder.
# gcd(4,36) => 4
# http://www.cse.wustl.edu/~kjg/cse131/Notes/Recursion/recursion.html
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


def gcd(x, y):
    pass

# 15. Write a function that compares each character of two strings and returns true if
# both are identical.
# compareStr('house', 'houses') # false
# compareStr('tomato', 'tomato') # true


def compareStr(str1, str2):
    pass

# 16. Write a function that accepts a string and creates an array where each letter
# occupies an index of the array.


def createArray(str):
    pass

# 17. Reverse the order of an array


def reverseArr(array):
    pass

# 18. Create a new array with a given value and length.
# buildList(0,5) # [0,0,0,0,0]
# buildList(7,3) # [7,7,7]


def buildList(value, length):
    pass

# 19. Implement FizzBuzz. Given integer n, return an array of the string representations of 1 to n.
# For multiples of three, output 'Fizz' instead of the number.
# For multiples of five, output 'Buzz' instead of the number.
# For numbers which are multiples of both three and five, output “FizzBuzz” instead of the number.
# fizzBuzz(5) # ['1','2','Fizz','4','Buzz']


def fizzBuzz(n):
    pass

# 20. Count the occurrence of a value in a list.
# countOccurrence([2,7,4,4,1,4], 4) # 3
# countOccurrence([2,'banana',4,4,1,'banana'], 'banana') # 2


def countOccurrence(array, value):
    pass

# 21. Write a recursive version of map.
# rMap([1,2,3], timesTwo) => [2,4,6]


def rMap(array, callback):
    pass

# 22. Write a function that counts the number of times a key occurs in an object.
# var obj = {'e':{'x':'y'},'t':{'r':{'e':'r'},'p':{'y':'r'}},'y':'e'};
# countKeysInObj(obj, 'r') # 1
# countKeysInObj(obj, 'e') # 2


def countKeysInObj(obj, key):
    pass

# 23. Write a function that counts the number of times a value occurs in an object.
# var obj = {'e':{'x':'y'},'t':{'r':{'e':'r'},'p':{'y':'r'}},'y':'e'};
# countValuesInObj(obj, 'r') # 2
# countValuesInObj(obj, 'e') # 1


def countValuesInObj(obj, value):
    pass

# 24. Find all keys in an object (and nested objects) by a provided name and rename
# them to a provided new name while preserving the value stored at that key.


def replaceKeysInObj(obj, oldKey, newKey):
    pass

# 25. Get the first n Fibonacci numbers. In the Fibonacci sequence, each subsequent
# number is the sum of the previous two.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.....
# fibonacci(5) => [0,1,1,2,3,5]
# Note: The 0 is not counted.


def fibonacci(n):
    pass

# 26. Return the Fibonacci number located at index n of the Fibonacci sequence.
# [0,1,1,2,3,5,8,13,21]
# nthFibo(5) => 5
# nthFibo(7) => 13
# nthFibo(3) => 2


def nthFibo(n):
    pass

# 27. Given an array of words, return a new array containing each word capitalized.
# var words = ['i', 'am', 'learning', 'recursion'];
# capitalizedWords(words) => ['I', 'AM', 'LEARNING', 'RECURSION']


def capitalizeWords(array):
    pass

# 28. Given an array of strings, capitalize the first letter of each index.
# capitalizeFirst(['car','poop','banana']) => ['Car','Poop','Banana']


def capitalizeFirst(array):
    pass

# 29. Return the sum of all even numbers in an object containing nested objects.
# var obj1 = {
#   a: 2,
#   b: {b: 2, bb: {b: 3, bb: {b: 2}}},
#   c: {c: {c: 2}, cc: 'ball', ccc: 5},
#   d: 1,
#   e: {e: {e: 2}, ee: 'car'}
# };
# nestedEvenSum(obj1) => 10


def nestedEvenSum(obj):
    pass

# 30. Flatten an array containing nested arrays.
# flatten([1,[2],[3,[[4]]],5]) => [1,2,3,4,5]


def flatten(array):
    pass

# 31. Given a string, return an object containing tallies of each letter.
# letterTally('potato') => {p:1, o:2, t:2, a:1}


def letterTally(str, obj):
    pass

# 32. Eliminate consecutive duplicates in a list. If the list contains repeated
# elements they should be replaced with a single copy of the element. The order of the
# elements should not be changed.
# compress([1,2,2,3,4,4,5,5,5]) # [1,2,3,4,5]
# compress([1,2,2,3,4,4,2,5,5,5,4,4]) # [1,2,3,4,2,5,4]


def compress(list):
    pass

# 33. Augment every element in a list with a new value where each element is an array
# itself.
# augmentElements([[],[3],[7]], 5) => [[5],[3,5],[7,5]]


def augmentElements(array, aug):
    pass

# 34. Reduce a series of zeroes to a single 0.
# minimizeZeroes([2,0,0,0,1,4]) # [2,0,1,4]
# minimizeZeroes([2,0,0,0,1,0,0,4]) # [2,0,1,0,4]


def minimizeZeroes(array):
    pass

# 35. Alternate the numbers in an array between positive and negative regardless of
# their original sign. The first number in the index always needs to be positive.
# alternateSign([2,7,8,3,1,4]) # [2,-7,8,-3,1,-4]
# alternateSign([-2,-7,8,3,-1,4]) # [2,-7,8,-3,1,-4]


def alternateSign(array):
    pass

# 36. Given a string, return a string with digits converted to their word equivalent.
# Assume all numbers are single digits (less than 10).
# numToText("I have 5 dogs and 6 ponies") => "I have five dogs and six ponies"


def numToText(str):
    pass


# *** EXTRA CREDIT ***

# 37. Return the number of times a tag occurs in the DOM.
def tagCount(tag, node):
    pass

# 38. Write a function for binary search.
# var array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
# binarySearch(array, 5) # 5
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search


def binarySearch(array, target, min, max):
    pass

# 39. Write a merge sort function.
# mergeSort([34,7,23,32,5,62]) # [5,7,23,32,34,62]
# https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/divide-and-conquer-algorithms


def mergeSort(array):
    pass

# 40. Deeply clone objects and arrays.
# var obj1 = {a:1,b:{bb:{bbb:2}},c:3};
# var obj2 = clone(obj1);
# console.log(obj2) => {a:1,b:{bb:{bbb:2}},c:3}
# obj1 === obj2 # false


def clone(input):
    pass
