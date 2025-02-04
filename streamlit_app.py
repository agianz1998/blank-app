import streamlit as st
import pandas as pd

st.title("🎈 Data Editor Test")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'Name':['Alice', 'Bob', 'Charlie'], 'Age':[20, 35, 42], 'status':[False, False, False]})
if 'edit_index' not in st.session_state:
    st.session_state.edit_index = None

for index, row in st.session_state.df.iterrows():
    cols = st.columns([3, 2, 3, 2])
    cols[0].write(row['Name'])
    cols[1].write(str(row['Age']))
    cols[2].write(row['status'])
    if cols[3].button('Edit', key=f"edit_{index}"):
        st.session_state.edit_index = index

#Edit Form
