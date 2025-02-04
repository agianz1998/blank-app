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
    cols = st.columns([3, 2, 3, 2, 2])
    cols[0].write(row['Name'])
    cols[1].write(str(row['Age']))
    cols[2].write(row['status'])
    cols[3].write("Yes" if row['status'] else "No")
    
    if cols[4].button('Edit', key=f"edit_{index}"):
        st.session_state.edit_index = index

#Edit Form
if st.session_state.edit_index is not None:
    index = st.session_state.edit_index
    row = st.session_state.df.loc[index]
    with st.form(key='edit_form'):
        st.header("Edit Entry")
        name = st.text_input("Name", value = row['Name'])
        age = st.number_input("Age", value = row['Age'])
        status = st.checkbox("Status", value = row['status'])

        col1, col2 = st.columns(2)
        if col1.form_submit_button('Save'):
            st.session_state.df.at[index, 'Name'] = name
            st.session_state.df.at[index, 'age'] = age
            st.session_state.df.at[index, 'status'] = status
            st.session_state.edit_index = None
            st.rerun()

        if col2.form_submit_button('Cancel'):
            st.session_state.edit_index = None
            st.rerun()

st.divider()
st.header("Currrent Data")
st.dataframe(st.session_state.df, use_container_width = True)
            
