import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly_express as px

#loading our dataset
df = pd.read_csv('vehicles_us.csv')

#creating a new column manufacturer by getting the first word from the model column
df['manufacturer'] = df['model'].apply(lambda x: 
x.split()[0]

#Creating texrt header above dataframe
st.header('Data viewer')

#Displaying dataframe with streamlit
st.dataframe(df)

###We want to view distribution of vehicle types by manufacturer

st.header('Vehicle types manufacturer')
#creating a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
#displaying figure w/ Streamlit
st.write(fig)

###Histogram of condition vs. model_year

st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)

###Comparing Price Distribution between manufacturers

##We need user input for First and Second manufacturer's names. Then filter dataframe to contain only those two manufacturers
#Creating Plotly histogram
st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)


