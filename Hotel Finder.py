import pandas as pd
import streamlit as st
from PIL import Image

import urllib.request

url = "https://raw.githubusercontent.com/BISMCA/Files/main/rev_sorted_short.csv"
rev_sort = pd.read_csv(url)

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Files/blob/e33c2ce8dbbf2e400cee59437aa8e5c15831fe6e/sort.jpg?raw=true',
   "sort.png")
img = Image.open("sort.png")
st.image(img, caption = 'Lets Travel')

st.title("Find your hotels")
st.write(
    """This app filters out and finds the hotels based on your requirement of stay in your hotel such as food, accommodation, commute,family friendliness, resort etc
    """)  

st.sidebar.write('Select Filter')
#Filter based on topic
cat_list = rev_sort.Topic.unique()
val = [None]* len(cat_list) # this list will store info about which category is selected
for i, cat in enumerate(cat_list):
    # create a checkbox for each category
    val[i] = st.sidebar.checkbox(cat, value=True) # value is the preselect value for first render

# filter data based on selection
dummy = rev_sort[rev_sort.Topic.isin(cat_list[val])].reset_index(drop=True)

#if dummy.shape[0]>0:
 #   st.dataframe(dummy)
#else:
  #  st.write("Empty Dataframe")

#blankIndex=['']*len(rev_sort)
#rev_sort.index=blankIndex

# #df = pd.read_csv(data_url)

#st.dataframe(dummy)
#Creating columns
col1,col2,col3 = st.columns(3)

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%201.png?raw=true',
   "img1.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%202.png?raw=true',
   "img2.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%203.png?raw=true',
   "img3.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%204.png?raw=true',
   "img4.png")


image1 = Image.open("img1.png")
image2 = Image.open("img2.png")
image3 = Image.open("img3.png")
image4 = Image.open("img4.png")
#Loading Hotels
with col1:
    m=0
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    st.image(image1, caption= 'Hotel 1', width = 100, use_column_width=100)
    
    st.write('rating:',star_rating)
    st.write('best known for:', topic)

with col3:
    m=1
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    st.image(image2, caption= 'Hotel 2', width = 100, use_column_width=100)
    
    st.write('rating:',star_rating)
    st.write('best known for:', topic)
    
with col1:
    m=2
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    st.image(image3, caption= 'Hotel 3', width = 100, use_column_width=100)
    
    st.write('rating:',star_rating)
    st.write('best known for:', topic)
    
with col3:
    m=3
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    st.image(image4, caption= 'Hotel 4', width = 100, use_column_width=100)
    
    st.write('rating:',star_rating)
    st.write('best known for:', topic)


