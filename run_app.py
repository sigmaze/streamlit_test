import streamlit as st

# Title of the web app
st.title('File Upload Example')

# Upload a file
uploaded_file = st.file_uploader("Choose a file")

# If a file is uploaded
if uploaded_file is not None:
    # Read and display the contents of the file
    file_contents = uploaded_file.read()
    st.write(file_contents)