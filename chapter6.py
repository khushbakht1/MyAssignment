#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string data type
str1="Hello"
str2="there"
bob=str1+str2
print(bob)


# In[2]:


str3='123'
str3=str3+1


# In[3]:


x=int(str3)+1
print(x)


# In[4]:


#reading and converting
name=input("Enter:")


# In[5]:


print(name)


# In[6]:


apple=input('Enter:')


# In[7]:


x=apple-10


# In[8]:


x=int(apple)-10
print(x)


# In[9]:


#looking inside strings
fruit='banana'
letter=fruit[1]
print(letter)


# In[10]:


x=3
w=fruit[x-1]
print(w)


# In[11]:


#a character too far
zot='abc'
print(zot[5])


# In[12]:


#strings have length
fruit='banana'
print(len(fruit))


# In[14]:


#len function
fruit='banana'
x=(len(fruit))
print(x)


# In[15]:


#looping through strings
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1


# In[16]:


#looping through strings
fruit='banana'
for letter in fruit:
    print(letter)


# In[20]:


fruit='banana'
for letter in fruit:
    print(letter)
index=0
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1


# In[21]:


#looping and counting
word='banana'
count=0
for letter in word:
    if letter =='a':
        count=count+1
print(count)


# In[22]:


#looking deeper into in
for letter in 'banana':
    print(letter)


# In[23]:


#slicing strings
s='Monty Python'
print(s[0:4])


# In[24]:


print(s[6:7])


# In[25]:


print(s[6:20])


# In[26]:


print(s[:2])


# In[27]:


print(s[8:])


# In[28]:


print(s[:])


# In[29]:


#string concatenation
a='Hello'
b=a+'There'
print(b)


# In[31]:


c=a+' '+'There'
print(c)


# In[32]:


#using in as logical operator
fruit='banana'
'n'in fruit


# In[33]:


'm'in fruit


# In[34]:


'nan'in fruit


# In[35]:


if'a'in fruit:
    print("Found it!")


# In[36]:


#string comparison
if word=='banana':
    print('All right, bananas.')
if word<'banana':
    print('Your word,'+word+',comes before banana.')
elif word>'banana':
    print('Your word,'+word+',comes after banana.')
else:
    print('All right,bananas.')
    


# In[37]:


#string library
greet="Hello Bob"
zap=greet.lower()
print(zap)


# In[38]:


print(greet)


# In[39]:


print('Hi There'.lower())


# In[42]:


stuff='Hello World'
type(stuff)
dir(stuff)


# In[43]:


#searching a string
fruit='banana'
pos=fruit.find('na')
print(pos)


# In[44]:


aa=fruit.find('z')
print(aa)


# In[45]:


#making everything uppercase
greet='Hello Bob'
nnn=greet.upper()
print(nnn)


# In[46]:


www=greet.lower()
print(www)


# In[47]:


#search and replace
greet='Hello Bob'
nstr=greet.replace('Bob','Jane')
print(nstr)


# In[48]:


nstr=greet.replace('o','x')
print(nstr)


# In[49]:


#stripping whitespace
greet=' Hello Bob '
greet.lstrip()


# In[50]:


greet.rstrip()


# In[51]:


greet.strip()


# In[53]:


#Prefixes
line='Please have a nice day'
line.startswith("Please")


# In[54]:


line.startswith('p')


# In[55]:


#parsing and extracting
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)


# In[57]:


sppos=data.find(' ',atpos)
print(sppos)


# In[58]:


host=data[atpos+1:sppos]
print(host)


# In[ ]:




