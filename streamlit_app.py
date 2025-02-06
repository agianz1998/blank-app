import streamlit as st
import pandas as pd


st.title("🎈 Data Editor Test")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

if 'selected_row' not in st.session_state:
    st.session_state.selected_row = None

data = pd.DataFrame({'Name':['Alice', 'Bob', 'Charlie'], 'City':['Chicago', 'Boston', 'Dallas'],'Active':['N', 'N', 'Y']})

st.markdown("""
<style>
    .styled-table {
        width: 100%;
        border-collapse: collapse;
    }
    .styled-table th, .styled-table td {
        border: 1px solid black;
        padding: 10px;
        test-align: left;
    }
    .styled-table th {
        background-color: #f2f2f2;
    }
</style>
""", unsafe_allow_html=True)

st.write("User Data Table:")
table_html = """
<table class ="styled-table">
    <tr>
        <th>Name</th>
        <th>City</th>
        <th>Active Status</th>
        <th>Edit</th>
    </tr>
"""

for index, row in data.iterrows():
    active_status = "Active" if row["Active"] == "Y" else "Inactive"
    table_html += f"""
    <tr>
        <td>{row['Name']}</td>
        <td>{row['City']}</td>
        <td>{active_status}</td>
        <td><b>[ Edit Row {index} ]</b></td>
    </tr>
    """
table_html += "</table>"

st.markdown(table_html, unsafe_allow_html=True)

for index, row in data.iterrows():
    if st.button(f"Edit Row {index}", key=f"edit_{index}"):
        st.session_state.selected_row = index

        

############################################################################
#if 'df' not in st.session_state:
#    st.session_state.df = pd.DataFrame({'Name':['Alice', 'Bob', 'Charlie'], 'Age':[20, 35, 42], 'City':['New York', 'London', 'Paris'], 'Active':[False, False, False], 'Actions':['Edit'] * 3})
#if 'edit_index' not in st.session_state:
#    st.session_state.edit_index = None

#edited_data = st.data_editor(st.session_state.df, 
#                             column_config = {
#                                 "Actions": {
#                                     "width": "small",
#                                     "help": "Click to edit this row",
#                                     "disabled": False
#                                 },
#                                 "Active":{
#                                     "help": "Account Status",
#                                     "disabled":True
#                                 }
#                             },
#                             hide_index = True,
#                             use_container_width = True,
#                             key = "main_editor"
#                            )

#if st.session_state.get("main_editor") is not None:
#    for index, row in st.session_state.df.iterrows():
#        if "Edit" in st.session_state.main_editor["edited_rows"].get(str(index),{}).values():
#            st.session_state.edit_index = index
#            break

#if st.session_state.edit_index is not None:
#    index = st.session_state.edit_index
#    row = st.session_state.df.loc[index]
#    with st.form(key='edit_form'):
#        st.subheader(f"Editing Row {index + 1}")
#        col1, col2 = st.columns(2)

#        with col1:
#            name = st.text_input("Name", value = row['Name'])
#            city = st.text_input("City", value = row['City'])

#        with col2:
#            age = st.number_input("Age", value = row['Age'])
#            active = st.checkbox("Active", value = row['Active'], disabled = row['Active'])
#        save_col, cancel_col = st.columns([1,4])
#        with save_col:
#            save = st.form_submit_button("Save")
#        with cancel_col:
#            cancel = st.form_submit_button("Cancel")

#        if save:
#            st.session_state.df.at[index, 'Name'] = name
#            st.session_state.df.at[index, 'Age'] = age
#            st.session_state.df.at[index, 'City'] = city
#            if not row['Active']:
#                st.session_state.df.at[index, 'Active'] = active
#            st.session_state.edit_index = None
#            st.rerun()

#        if cancel:
#            st.session_state.edit_index = None
#            st.rerun()
            

    



#for index, row in st.session_state.df.iterrows():
#    cols = st.columns([5,3,4,3,3])
#    cols[0].write(row['Name'])
#    cols[1].write(str(row['Age']))
#    cols[2].write(row['status'])
#    cols[3].write("Yes" if row['status'] else "No")
    
#    if cols[4].button('Edit', key=f"edit_{index}"):
#        st.session_state.edit_index = index

#Edit Form
#if st.session_state.edit_index is not None:
#    index = st.session_state.edit_index
#    row = st.session_state.df.loc[index]
#    with st.form(key='edit_form'):
#        st.header("Edit Entry")
#        name = st.text_input("Name", value = row['Name'])
#        age = st.number_input("Age", value = row['Age'])
#        status = st.checkbox("Status", value = row['status'], disabled=row['status'])

#       col1, col2 = st.columns(2)
#       if col1.form_submit_button('Save'):
#           st.session_state.df.at[index, 'Name'] = name
#           st.session_state.df.at[index, 'age'] = age
#           st.session_state.df.at[index, 'status'] = status
#           st.session_state.edit_index = None
#           st.rerun()

#        if col2.form_submit_button('Cancel'):
#            st.session_state.edit_index = None
#            st.rerun()

#st.divider()
#st.header("Currrent Data")
#st.dataframe(st.session_state.df, use_container_width = True)
            
