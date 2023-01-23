#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


arr = np.array([1,2,3])
arr


# In[4]:


list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
np.array(list_of_lists)


# In[6]:


np.arange(1,10)


# In[7]:


np.arange(20)


# In[8]:


np.arange(1,46,5)


# In[10]:


np.zeros(10)


# In[11]:


np.zeros(10,dtype=int)


# In[12]:


np.ones(10)


# In[13]:


#array of ones with 2 rows and 5 columns
np.ones((2,5))


# In[14]:


####creating an array with 2 rows and 10 columns
np.zeros((2,10))


# In[16]:


#dividing range in equal parts
np.linspace(0,1,4)
np.linspace(0,20,8)


# In[17]:


#creates identity matrix
np.eye(5)


# In[18]:


np.random.rand(3,2)


# In[20]:


np.random.randint(3,10)


# In[21]:


np.random.randint(5,20,5)


# In[23]:


sarray = np.arange(30)
sarray


# In[33]:


#we can only reshape when elements of array = total elements of the new matrix
tarray = sarray.reshape(5,6)
tarray


# In[27]:


sarray.min()


# In[28]:


sarray.argmin()


# In[29]:


sarray.max()


# In[30]:


sarray.argmax()


# In[34]:


#to have transpose of a matrix
tarray.T


# In[35]:


tarray[2:5]


# In[37]:


arr[1:3]=100
arr


# In[38]:


#2 DIMENSIONAL ARRAY
sample_matrix = np.array(([2,5,4,3],[24,53,12,54],[65,22,10,8]))
sample_matrix


# In[39]:


sample_matrix[2][1]


# In[40]:


sample_matrix[2:]


# In[41]:


#here an array with 3 rows and 2 columns will be formed and it'll have its elements from all lists with there 
#3rd index one its first and 2nd index one as its second
sample_matrix[:,(3,2)]


# In[ ]:


#SELECTION TECHNIQUES


# In[42]:


sample_array = np.arange(20)
sample_array


# In[43]:


sample_array + sample_array


# In[44]:


sample_array*2


# In[45]:


np.exp(sample_array)#exponential of al elements


# In[46]:


np.sqrt(sample_array)#square root of all elements


# In[47]:


np.log(sample_array)#log of all elements


# In[ ]:


#max, min and there arguement one is known


# In[ ]:


np.var(sample_array)#will give variance
np.mean(sample_array)#will give mean
np.round(sample_array)#will round it of


# In[48]:


sp = np.array(['soccer','cricket','soccer','squash','tennis'])
np.unique(sp)#will omit any repetition of elements and dtype gives length of longest string when string used


# In[ ]:




