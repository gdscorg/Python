#!/usr/bin/env python
# coding: utf-8

# In[2]:


#decimal to grey
#wrong code
num=int(input("enter an integer"))
l=[]
while(num>0):
    rem=num%2
    l.append(rem)
    num=num//10
l=l[:]
gray=[]

gray.append(l[1])
i=0
while(i+1<(len(l))):
    a=(l[i] ^ l[i+1])
    gray.append(a)
    i=i+1
for i in gray:
    print(i,end='')


# In[ ]:




