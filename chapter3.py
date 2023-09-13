#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Conditional steps:
x=5
if x<10:
    print('Smaller')
if x>20:
    print('Bigger')
print('Finis')


# In[2]:


#comparison operators
x=5
if x==5:
    print('Equals 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or Equals 5')
if x<6:
    print('Less than 6')
if x<=5:
    print('Less than or Equals 5')
if x!=6:
    print('Not equal 6')


# In[3]:


#One-way decisions
x=5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x==6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')


# In[5]:


#Indentation
x=5
if x>2:
    print('Bigger Than 2')
    print('Still Bigger')
print('Done with 2')
for i in range(5):
    print(i)
    if i>2:
        print('Bigger Than 2')
    print('Done with i',i)
print('Áll Done')


# In[6]:


#Nested Decisions
x=42
if x>1:
    print('More than one')
    if x<100:
        print('Less than 100')
print('Áll done')


# In[7]:


#Two way decisions with else
x=4
if x>2:
    print('Bigger')
else:
    print('Smaller')
print('All done')


# In[8]:


#Multiway
if x<2:
    print('small')
elif x<10:
    print('Medium')
else:
    print('Large')
print('All done')


# In[9]:


#Multiway
if x<2:
    print('small')
elif x<10:
    print('Medium')
elif x<20:
    print('Big')
elif x<40:
    print('Large')
elif x<100:
    print('Huge')
else:
    print('Ginormous')


# In[10]:


#Multiway puzzles
if x<2:
    print('Below 2')
elif x<20:
    print('Below 20')
elif x<10:
    print('Below 10')
else:
    print('Something else')


# In[11]:


astr='Hello Bob'
istr=int(astr)
print('First',istr)
astr='123'
istr=int(astr)
print('Second',istr)


# In[12]:


#the try/except structure
astr='Hello Bob'
try:
    istr=int(astr)
except:
    istr=-1
print('First',istr)
astr='123'
try:
    istr=int(astr)
except:
    istr=-1
print('Second',istr)


# In[13]:


astr='Bob'
try:
    print('Hello')
    istr=int(astr)
    print('There')
except:
    istr=-1
print('Done',istr)


# In[16]:


rawstr=input('Enter a number:')
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print('Nice work')
else:
    print('Not a number')
    


# In[23]:


#Exercise
hours=float(input('Enter Hours: '))
rate=float(input('Enter Rate: '))
if hours<=40:
    pay=hours*rate
else:
    regular_pay=40*rate
    overtime_pay=(hours-40)*(rate*1.5)
    pay=regular_pay+overtime_pay
print('Pay:',pay)


# In[25]:


#Exercise
try:
    hours=float(input('Enter Hours: '))
    rate=float(input('Enter Rate: '))
    if hours<=40:
        pay=hours*rate
    else:
        regular_pay=40*rate
        overtime_pay=(hours-40)*(rate*1.5)
        pay=regular_pay+overtime_pay
    print('Pay:',pay)
except:
    print('Error, Enter Numeric Input')
    
    


# In[ ]:





# In[ ]:




