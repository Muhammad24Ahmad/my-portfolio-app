import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Muhammad Ahmad")
    content = """
    Hi, I am Muhammad Ahmad. I am Software Trainee Engineer at CureMD. I graduated in June, 
    2024 with the degree of BS Computer Engineering from Information Technology University of the Punjab, Lahore.
    """
    st.write(content)