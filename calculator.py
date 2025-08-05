import streamlit as st
st.title("Simple Calculator")
st.subheader("Built with Streamlit")
st.markdown("This is a simple calculator app built with Streamlit.")

c1,c2 = st.columns(2)
fnum = c1.number_input("First Number", value=0)
snum = c2.number_input("Second Number", value=0)

options = ["Add", "Sbtract", "Multiply", "Divide"]
choice = st.radio("Select Operation", options)

button = st.button ("Calculate")

result = 0
if button:
    if choice == "Add":
        result = fnum+snum
    if choice == "Sbtract":
        result = fnum-snum
    if choice == "Multiply":
        result = fnum*snum
    if choice == "Divide":
        result = fnum/snum 

st.success(f'Result: {result}')