#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')
# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)


# In[2]:


print(123)


# In[3]:


print(98.6)


# In[4]:


print('hello world')


# In[5]:


x1q3z9ocd = 35.0
x1q3z9afd = 12.50
x1q3p9afd =  x1q3z9ocd * x1q3z9afd
print(x1q3p9afd)


# In[6]:


a = 35.0
b = 12.50
c = a * b
print(c)


# In[7]:


hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)


# In[8]:


print(float(99)+100)


# In[9]:


i = 42
type(i)


# In[10]:


i = 42
type(i)
f = float(i)
print(f)


# In[11]:


nam = input('who are you? ')
print('welcome', nam)


# In[12]:


inp =input('europe floor?')
usf =int(inp) + 1
print('us floor',usf)


# In[13]:


# Prompt the user for hours and rate per hour
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Calculate gross pay
gross_pay = hours * rate

# Display the result
print("Pay:", gross_pay)


# In[ ]:




