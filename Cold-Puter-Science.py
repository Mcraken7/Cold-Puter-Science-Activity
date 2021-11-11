#!/usr/bin/env python
# coding: utf-8

# ## Cold-Puter-Science

# In[22]:


import sys
print("Enter a number")

result = 0

numTemps = int(input())
print("Enter " + str(numTemps) + " Temperature numbers")

numbers = input().split()

for number in numbers:

    if int(number) < 0:
        result += 1
print("---------------------------------------------------")
print ("There are " + str(result) + " Cold Temperatures")
print ("The values are " + str(numbers))


# In[ ]:





# In[ ]:




