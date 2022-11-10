#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv
from scipy import ndimage


# In[3]:


#to read/load image
img1=cv.imread('img1.jpg')


# In[4]:


#to see image
cv.imshow('orginal_image',img1)
cv.waitKey(0)
cv.destroyAllWindows()


# In[5]:


#shape of the image
print(img1.shape)


# In[20]:


#splitting image into 4 by using pixel values
#run another code on different window to get these axis values of image
rectangle1=img1[128:251,149:386] #pixel rows and columns
rectangle2=img1[115:289,466:707]
rectangle3=img1[360:563,102:350]
rectangle4=img1[351:604,461:740]


# In[23]:


#manually rotating image by degress
rot1=ndimage.rotate(rectangle1,17)
rot2=ndimage.rotate(rectangle2,345)
rot3=ndimage.rotate(rectangle3,-30)
rot4=ndimage.rotate(rectangle4,30)

#rotated image dialog box
cv.imshow('rotated_rec1',rot1)
cv.imshow('rotated_rec2',rot2)
cv.imshow('rotated_rec3',rot3)
cv.imshow('rotated_rec4',rot4)
cv.waitKey(0)
cv.destroyAllWindows()


# In[21]:





# In[ ]:




