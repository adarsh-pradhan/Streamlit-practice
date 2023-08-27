import streamlit as st


st.write("""
# Finding the largest number
""")

st.header("Input three number below:")

def user_input_features():
    num_1 = st.number_input("Number 1")
    num_2 = st.number_input("Number 2")
    num_3 = st.number_input("Number 3")
    
    data = [num_1, num_2, num_3]
    
    return data

nums = user_input_features()

st.subheader("The largest of the above three numbers is: " + max(nums))
