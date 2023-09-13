#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Loops and Iteration
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)


# In[ ]:


#Infinite Loop
n=5
while n>0:
    print('Lather')
    print('Rinse')
print('Dry off!')


# In[1]:


#Another Loop
n=0
while n>0:
    print('Lather')
    print('Rinse')
print('Dry off!')


# In[2]:


#Breaking out of a loop
while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done!')


# In[1]:


#Finishing an iteration with continue
while True:
    line=input('>')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('Done!')


# In[2]:


#A simple definite Loop
for i in[5,4,3,2,1]:
    print(i)
print('Blastoff!')


# In[3]:


#A definite loop with strings
friends=['Joseph','Glenn','Sally']
for friend in friends:
    print('Happy New Year:',friend)
print('Done!')


# In[4]:


#looping through a set
print('Before')
for thing in[9,41,12,3,74,15]:
    print(thing)
print('After')


# In[5]:


#Finding the largest value
largest_so_far=-1
print('Before',largest_so_far)
for the_num in[9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far, the_num)
print('After',largest_so_far)


# In[6]:


#Counting in a loop
zork=0
print('Before',zork)
for thing in[9,41,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
print('After',zork)


# In[7]:


#Summing in a loop
zork=0
print('Before',zork)
for thing in[9,41,12,3,74,15]:
    zork=zork+thing
    print(zork,thing)
print('After',zork)


# In[8]:


#Finding the average in a loop
count=0
sum=0
print('Before',count,sum)
for value in[9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
print('After',count,sum,sum/count)


# In[9]:


#filtering in a loop
print('Before')
for value in[9,41,12,3,74,15]:
    if value>20:
        print('Large number',value)
print('After')


# In[10]:


#Search using a boolean variable
found=False
print('Before',found)
for value in[9,41,12,3,74,15]:
    if value==3:
        found=True
    print(found,value)
print('After',found)


# In[11]:


#Finding the smallest value
smallest_so_far=-1
print('Before',smallest_so_far)
for the_num in[9,41,12,3,74,15]:
    if the_num<smallest_so_far:
        smallest_so_far=the_num
    print(smallest_so_far, the_num)
print('After',smallest_so_far)


# In[12]:


smallest=None
print('Before')
for value in[9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('After',smallest)


# In[13]:


#This is and is not operators
smallest=None
print('Before')
for value in[3,41,12,9,74,15]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('After',smallest)


# In[ ]:




