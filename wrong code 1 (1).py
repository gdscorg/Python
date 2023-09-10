#!/usr/bin/env python
# coding: utf-8

# In[36]:


#wrong code
#how many characters are repeating in the given string
class textanalyzer(object):
    def __init__(self,text):
        ft=text.replace(',','').replace('.','').replace('!','').replace('?','')
        ft=ft.lower()
        self.ft=ft
    def freqall(self):
        wordlist=ft.split(" ")
        freqmap={}
        for word in (wordlist):
            freqmap[word]=wordlist.count(word)
        return freqmap
    def freqof():
        freqdict=self.freqall()
        if word in freqdict:
            return( freqdict[word])
        else:
            return( 0)
analyzed=textanalyzer("hello, how how are you")
freqMap=analyzed.freqall()
freqof_how=analyzed.freqof("how")
print(freqof_how)


# In[18]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




