#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = int(input ("enter number of terms to print Fibonacci series? "))  
  

f = 0  
s = 1  
count = 0  
  
if number <= 0:  
    print ("Please enter a correct integer")  
  
elif number == 1:  
    print ("The Fibonacci sequence of the numbers up to", f, ": ")  
    print(f)  

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < number:  
        print(f)  
        n = f + s  
        
        f = s  
        s = n  
        count += 1


# In[ ]:




