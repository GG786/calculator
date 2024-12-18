import streamlit as st

# Streamlit app title
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Dropdown for operation selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 == 0:
            st.error("Error: Division by zero")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")
