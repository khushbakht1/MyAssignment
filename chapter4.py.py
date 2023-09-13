#!/usr/bin/env python
# coding: utf-8

# In[1]:


sval = '123'
# Assign the string '123' to the variable sval.

type(sval)
# Check the type of sval, which is a string (str).

print(sval + '1')
# This line concatenates the string sval with the string '1'.
# This will print '1231'.

ival = int(sval)
# Convert the string sval to an integer and assign it to the variable ival.

type(ival)
# Check the type of ival, which is now an integer (int).

print(ival + 1)
# Add 1 to the integer ival and print the result, which is 124.

nsv = 'hello bob'
# Assign the string 'hello bob' to the variable nsv.

# The following line attempts to convert the string nsv to an integer,
# but it raises a ValueError because 'hello bob' is not a valid integer literal.
# You cannot convert this string to an integer.


# In[2]:


x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()  # Call the print_lyrics function
x = x + 2
print(x)


# In[3]:


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')  # Calls greet with 'en' as the argument, which prints 'Hello'
greet('es')  # Calls greet with 'es' as the argument, which prints 'Hola'
greet('fr')  # Calls greet with 'fr' as the argument, which prints 'Bonjour'


# In[4]:


def greet():
    return "Hello"

print(greet(), "Glenn")  # Calls greet(), which returns "Hello", and prints "Hello Glenn"
print(greet(), "Sally")  # Calls greet(), which returns "Hello", and prints "Hello Sally"


# In[5]:


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')  # Calls greet('en') and prints "Hello Glenn"
print(greet('es'), 'Sally')  # Calls greet('es') and prints "Hola Sally"
print(greet('fr'), 'Michael')  # Calls greet('fr') and prints "Bonjour Michael"


# In[6]:


def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


# In[7]:


x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)


# In[8]:


# Calculate and print the result of the expressions
result1 = float(99) / 100
print(result1)  # Output: 0.99

i = 42
print(type(i))  # Output: <class 'int'>

f = float(i)
print(f)  # Output: 42.0

print(type(f))  # Output: <class 'float'>

result2 = 1 + 2 * float(3) / 4 - 5
print(result2)  # Output: -2.5


# In[9]:


big = max('Hello world')
print(big)

tiny = min('Hello world')
print(tiny)


# In[10]:


big = max('Hello world')
print(big)


# In[11]:


def thing():
    print('Hello')
    print('Fun')

thing()  # Call the function and print "Hello" and "Fun"
print('Zip')
thing()  # Call the function again and print "Hello" and "Fun"


# In[ ]:




