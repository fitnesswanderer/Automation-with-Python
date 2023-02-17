#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


import pyperclip, re


# ## Strong Password Detection
# 
# Write a function that uses regular expressions to make sure the password 
# string it is passed is strong. A strong password is defined as one that is at 
# least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.

# In[3]:


passregex = re.compile(r'''
.{8,}                       # at -least 8 digit
(.*?[A-Z]|.*?[a-z].*?[A-Z]) #at least one lower case and uppercase character
(.*?[0-9].*?[!@#$&*_])      #at least one digit and a special character
(.*?[0-9]|.*?[a-z]|.*?[A-Z]) # at least one digit or an uppercase or lower case character after special character                 
 ''', re.VERBOSE)


# In[4]:


def PasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passregex.search(ppass)
    if (not mo):
        print("Not strong, ")
        return False
    else:
        print("Strong password,Bingo")
        return True


# In[5]:




PasswordCheck()


# In[6]:


PasswordCheck()


# In[7]:


PasswordCheck()


# In[8]:


PasswordCheck()


# In[ ]:




