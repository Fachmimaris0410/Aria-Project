import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.title("--Target Prediction--")


# Step 1 - import saved model
model = pickle.load(open("target_pred.pkl", "rb"))

st.write('Insert feature to predict')

# Step 2 - prepare input data for user

v1 = st.number_input('v1')
st.write('The current number is ', v1)
v2 = st.number_input('v2')
st.write('The current number is ', v2)
v3 = st.number_input('v3')
st.write('The current number is ', v3)
v4 = st.number_input('v4')
st.write('The current number is ', v4)
v5 = st.number_input('v5')
st.write('The current number is ', v5)
v6 = st.number_input('v6')
st.write('The current number is ', v6)
v7 = st.number_input('v7')
st.write('The current number is ', v7)
v8 = st.number_input('v8')
st.write('The current number is ', v8)
Sample_type = st.selectbox(label='Sample Type', options=['Lab 1', 'Lab 2'])



# convert into dataframe
data = pd.DataFrame({'v1':[v1],
 'v2':[v2],
 'v3':[v3],
 'v4':[v4],
 'v5':[v5],
 'v6':[v6],
 'v7':[v7],
 'v8': [v8],
 'Sample_type':[Sample_type]
                })
st.write(data)
# model predict
clas = model.predict(data).tolist()[0]

# interpretation
st.write('Target Prediction Result: ',clas)
