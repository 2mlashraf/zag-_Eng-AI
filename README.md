# Python Basics

This document contains fundamental concepts in Python, including string manipulation, functions, conditions, and object-oriented programming.

## 1. String Manipulation

### 1.1 Indexing
You can access a single character in a string using indexing:
```python
mystring = "hello python"
print(mystring[0])   # Output: h
print(mystring[-1])  # Output: n
```
1.2 Slicing
You can access multiple characters using the [start:end] format (the end is not included)
```python
print(mystring[:10])      # Output: hello pyt
print(mystring[::2])      # Output: hlopto
```
2. String Methods
len(): Returns the length of the string.
strip(): Removes extra spaces from both ends.
split(): Splits the string into a list based on a delimiter.
upper() / lower(): Converts the string to uppercase or lowercase.
replace(): Replaces a part of the string with another.
find(): Searches for a substring and returns its index.
join(): Joins list elements into a string using a specified delimiter.
format() / f-strings: Used for formatting strings.

3. Comments
Single-line comments start with #.
Triple quotes can be used for multi-line comments, but they are not comments unless assigned to a variable.

4. Functions
4.1 Defining Functions
Use the def keyword to define a function
```python
def greet(name):
    print(f"Hello, {name}!")
```
4.2 Calling Functions
You can call a function using its name and passing arguments
```python
greet('Alice')  # Output: Hello, Alice!
```
4.3 Parameters
Functions can take multiple parameters
```python
def add(x, y):
    return x + y
```
4.4 Return Values
Use the return keyword to return a value
```python
def multiply(x, y):
    return x * y
```
4.5 Nested Functions
You can define a function inside another function
```python
def outer_function():
    def inner_function():
        return "Hello from inner!"
    return inner_function()
```
4.6 Recursive Functions
A function can call itself
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
5. Conditions
5.1 If Statements
A block of code is executed if the condition is true
```python
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
```
5.2 Else Statements
An else statement can be used to execute a block if the condition is false.

5.3 Elif Statements
You can check multiple conditions
```python
if condition1:
    # Code if condition1 is true
elif condition2:
    # Code if condition2 is true
else:
    # Code if both conditions are false
```
5.4 Nested Conditions
if statements can contain other if statements inside them.

5.5 Logical Operators
You can combine conditions using operators:

and: Returns true if all conditions are true.
or: Returns true if at least one condition is true.
not: Negates the condition's result.

6. Object-Oriented Programming (OOP)
6.1 Objects
An object is an instance of a class that contains data (attributes) and behaviors (methods).

6.2 Classes
A class is a blueprint for creating objects, containing attributes and methods
```python
class Student:
    def __init__(self, name):
        self.name = name
```
6.3 Attributes
Attributes are variables associated with an object.

6.4 Methods
Methods are functions defined within a class that operate on the object's data










