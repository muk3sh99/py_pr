#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2 as cv
from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt


# In[ ]:


#Reading image
img=cv.imread('img1.jpg')
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:


#splitting image into 4 by using pixel values
rectangle1=img[128:251,149:386] #pixel rows and columns
rectangle2=img[115:289,466:707]
rectangle3=img[360:563,102:350]
rectangle4=img[351:604,461:740]


# In[ ]:


#manually rotating image by degress
rot1=ndimage.rotate(rectangle1,17)
rot2=ndimage.rotate(rectangle2,345)
rot3=ndimage.rotate(rectangle3,-30)
rot4=ndimage.rotate(rectangle4,30)


# In[ ]:


#resizing image same as 'rot1' to compare line lengh using pixel axis
rot2a=cv.resize(rot2,(263,187))
rot3a=cv.resize(rot3,(263,187))
rot4a=cv.resize(rot4,(263,187))


# In[ ]:


#testing whether the size got resize or not
print(rot1.shape)
print(rot2a.shape)


# In[ ]:


#plotting reshaped rectangle
plt.figure(figsize=(11,11))
plt.imshow(rot1)
plt.title('rectangle1')
plt.xlabel(rot1.shape[1],fontsize=10)
plt.ylabel(rot1.shape[0],fontsize=10)


# In[ ]:


plt.figure(figsize=(11,11))
plt.imshow(rot2a)
plt.title('rectangle2')
plt.xlabel(rot2a.shape[1],fontsize=10)
plt.ylabel(rot2a.shape[0],fontsize=10)


# In[ ]:


plt.figure(figsize=(11,11))
plt.imshow(rot3a)
plt.title('rectangle3')
plt.xlabel(rot3a.shape[1],fontsize=10)
plt.ylabel(rot3a.shape[0],fontsize=10)


# In[ ]:


plt.figure(figsize=(11,11))
plt.imshow(rot4a)
plt.title('rectangle4')
plt.xlabel(rot4a.shape[1],fontsize=10)
plt.ylabel(rot4a.shape[0],fontsize=10)


# By looking at these plots, I conclude that:
# • Line inside Rectangle1 starts at about 75 Pixel and ends at about 160 Pixel. Thus, the length of the line is about 85.
# • In Rectangle2 the line starts at about 80 Pixel and ends at about 200 Pixel. Thus, the length of line is about 120.
# • In Rectangle3 the line starts at about 70 Pixel and ends at about 220 Pixel. Thus, the length of line is about 150.
# • In Rectangle4 the line starts at about 80 Pixel and ends at about 140 Pixel. Thus, the length of line is about 60.
# 

# In[ ]:


#Numbering rectangle as per line length.
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('img1.jpg')

# Call draw Method to add 2D graphics in an image
T1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('arial.ttf', 65)

# Add number to an image
T1.text((607, 600), "1", font=myFont, fill =(255, 0, 0))
T1.text((255, 215), "2", font=myFont, fill =(255, 0, 0))
T1.text((630, 230), "3", font=myFont, fill =(255, 0, 0))
T1.text((200, 500), "4", font=myFont, fill =(255, 0, 0))

# Display edited image
img.show()

#save image
img.save("numbered.jpg")

 

