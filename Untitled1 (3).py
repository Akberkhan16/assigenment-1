#!/usr/bin/env python
# coding: utf-8

# In[19]:


def reverse (s):
    str = ""
    for i in s :
        str = i + str
    return str
    
print("please enter the input word")
word =input()

print("the original string is:",end="")
print(word)

print("the reversed string(using loops) is:",end="")
print(reverse(word))


# In[ ]:




