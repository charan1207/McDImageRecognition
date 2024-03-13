# -*- coding: utf-8 -*-
"""McDImageRecognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pCgZ3T5Ofa6wDylqpWmLs9okRwmQtPoc
"""

# Data :Images
!pip install bing-image-downloader

!mkdir images

from bing_image_downloader import downloader
downloader.download("big mac burger",limit=30,output_dir='images',adult_filter_off=True)

from bing_image_downloader import downloader
downloader.download("french fries",limit=30,output_dir='images',adult_filter_off=True)

downloader.download("nuggets",limit=30,output_dir='images',adult_filter_off=True)

#preprocessing
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

target=[]
images=[]
flat_data=[]

DATADIR = '/content/images'
CATEGORIES = ['big mac burger', 'french fries','nuggets']

for category in CATEGORIES:
  class_num=CATEGORIES.index(category)
  path=os.path.join(DATADIR,category)
  for img in os.listdir(path):
    img_array=imread(os.path.join(path,img))
    #plt.imshow(img_array)
    img_resized=resize(img_array,(150,150,3))
    flat_data.append(img_resized.flatten())
    images.append(img_resized)
    target.append(class_num)

flat_date=np.array(flat_data)
target = np.array(target)
images= np.array(images)

flat_data[0]

target

unique,count=np.unique(target,return_counts=True)
plt.bar(CATEGORIES,count)

np.unique(target,return_counts=True)

#split data into Traning and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(flat_data,target,test_size=0.3,random_state=109)

from sklearn.model_selection import GridSearchCV
from sklearn import svm
param_grid=[
    {'C':[1,10,100,1000],'kernel':['linear']},
    {'C':[1,10,100,1000],'gamma':[0.001,0.0001],'kernel':['rbf']},
]
svc=svm.SVC(probability=True)
clf=GridSearchCV(svc,param_grid)
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score,confusion_matrix

accuracy_score(y_pred,y_test)

confusion_matrix(y_pred,y_test)

#save pickle
import pickle
pickle.dump(clf,open('img_model.p','wb'))

model=pickle.load(open('img_model.p','rb'))

flat_data=[]
url=input('Enter your URL')
img=imread(url)
img_resized=resize(img,(150,150,3))
flat_data.append(img_resized.flatten())
flat_data=np.array(flat_data)
print(img.shape)
plt.imshow(img_resized)
y_out=model.predict(flat_data)
y_out=CATEGORIES[y_out[0]]
print(f'Predicted output:{y_out}')



!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import numpy as np
# from skimage.io import imread
# from skimage.transform import resize
# from PIL import Image
# import pickle
# 
# st.title("McDImageRecognition Machine Learning")
# st.text('Please Upload the Image')
# 
# model=pickle.load(open('img_model.p','rb'))
# 
# Uploaded_file=st.file_uploader("Choose an Image...",type="jpg")
# if(Uploaded_file is not None):
#   img=Image.open(Uploaded_file)
#   st.image(img,caption='Uploaded Image')
# 
#   if st.button('PREDICT'):
#       CATEGORIES = ['big mac burger', 'french fries','nuggets']
#       st.write('Result...')
#       flat_data=[]
#       img=np.array(img)
#       img_resized=resize(img,(150,150,3))
#       flat_data.append(img_resized.flatten())
#       flat_data=np.array(flat_data)
#       y_out=model.predict(flat_data)
#       y_out=CATEGORIES[y_out[0]]
#       st.title(f'Predicted output:{y_out}')
#       q=model.predict_proba(flat_data)
#       for index, item in enumerate(CATEGORIES):
#         st.write(f'{item}:{q[0][index]*100}%')
# 
# 
#

!wget -q -O - ipv4.icanhazip.com

!streamlit run app.py & npx localtunnel --port 8501