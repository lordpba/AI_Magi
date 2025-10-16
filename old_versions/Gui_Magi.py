import streamlit as st
from Main_core_refactor import process_question

# Streamlit application
st.title("Magi System Interface")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner('Processing...'):
        result = process_question(question)
        st.success('Done!')

        st.write("### Result")
        st.json(result)
