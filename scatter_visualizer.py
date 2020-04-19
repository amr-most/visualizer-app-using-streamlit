import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Creating a Title for the Project
st.title("Visualizer Proof of Concept")

# Creating a Data Frame of Random Values
a = np.random.randint(0 , 100 , 50)
b = 2*a
c = 3*a**.5
df = pd.DataFrame.from_dict({'a': a, 'b': b, 'c': c})

# Creating a Button to Display the Data Frame
if st.button('Show Data Frame'):
    st.dataframe(df)

# Getting the Column from the User
x = st.selectbox('Choose the first column you want to compare with: ', list(df.columns))
y = st.selectbox('Choose the second column you want to compare with: ', list(df.columns))

# Visualizing the Histogram
if st.button("Visualize scatter plot"):
    plt.figure(figsize=(10,10))
    plt.title(f"relation between x , y")
    plt.plot(df[x], df[y] , color='green')
    plt.savefig(f"{x}_histogram.png")
    st.pyplot()
