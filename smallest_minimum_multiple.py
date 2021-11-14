#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Initialize variables
cont = 1
end = False
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

while end==False:
    # Results list of results
    res = [cont % num_pos for num_pos in numbers]
    # Check if all remains are 0
    if res.count(0) == 10:
        print(f'The smallest positive number divisible by all of numbers from 1 to 20 is: {cont}')
        end = True
    cont+=1

