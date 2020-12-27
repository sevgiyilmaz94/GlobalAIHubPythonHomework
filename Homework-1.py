#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Takes 5 values from user
val1=input("Please write first value : ")
val2=input("Please write second value : ")
val3=input("Please write third value : ")
val4=input("Please write forth value : ")
val5=input("Please write fifth value : ")

#Print the values that user's input
values=[val1,val2,val3,val4,val5]
for i in values:  
    if type(i)==str:
        val_type="string"
    else:
        val_type="not_string"
        
    print('Type of values is %s '%val_type)

#Print values to screen
counter=1
for a in values:
    print("Your {}.values is {}".format(counter,values[counter-1]))
    counter+=1


# In[ ]:




