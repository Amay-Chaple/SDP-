

import streamlit as st;
import numpy as np;
import pandas as pd;

st.title("My First Streamlit app");
st.write("streamlit: Hello Vansh");
st.text("Lets start");

name = st.text_input("Enter name: ");
if st.button("Greet"):
    st.success(f"Hello, {name} !");

df = pd.DataFrame(np.random.randn(10, 2),columns=['A','B']);
st.line_chart(df);
st.bar_chart(df);

st.sidebar.title("Navigation");
st.image("https://th.bing.com/th?id=OVFT.BIwMDoe2cJvLgyogRgbyGS&pid=News&w=316&h=200&c=14&rs=2&qlt=90", caption="sample image");
st.video("https://www.youtube.com/shorts/zdmNssjcOLw?feature=share");

st.title("Text and Demo");
st.header("This is a header");
st.subheader("This is subheader");
st.markdown("Bold, Italic");
# st.code("for(int i=0;i<n;i++) cout << arr[i]", language="cpp");
st.code("for(int i=0;i<n;i++) cout << arr[i]", language="python");

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show details"):
    st.info("Here are more details...");

option = st.radio("Choose view", ["show chart", "show table"]);
if option == "show chart":
    st.write("chart would appeare here");
else :
    st.write("table would appear here");


with st.form("login_form"):
    username = st.text_input("Username");
    password = st.text_input("Password", type="password");
    submitted = st.form_submit_button("Login");

if submitted:
    st.success(f"Welcom, {username} !");

col1, col2 = st.columns(2);
with col1:
    st.button("Press colum 1");
with col2 :
    st.button("Press colum 2");

with st.expander("See explanation"):
    st.write("Here is hidden msg inside expander");

import matplotlib.pyplot as plt

fig, ax = plt.subplots();
ax.plot([1,2,4],[5,4,1]);
st.pyplot(fig);

import plotly.express as px

df = px.data.iris();
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species");
st.plotly_chart(fig);