import streamlit as st
import pandas as pd

def paginate_dataframe(df, page_size):
    if 'page_num' not in st.session_state:
        st.session_state.page_num = 1
#    page_num = st.session_state.get('page_num', 1)
    page_num = st.session_state.page_num
    if 'next' in st.button('Next'):
        page_num += 1
    elif 'prev' in st.button('Previous'):
        page_num -= 1
    st.session_state['page_num'] = page_num
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    return df.iloc[start_idx:end_idx]

# Example usage
#df = pd.DataFrame({'data': range(1, 1001)})
#page_size = 10
#paged_df = paginate_dataframe(df, page_size)
#st.dataframe(paged_df)


st.title("🎈 Data Editor Test")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

if 'selected_row' not in st.session_state:
    st.session_state.selected_row = None

if 'selected_index' not in st.session_state:
    st.session_state.selected_index = 0

#data = pd.DataFrame({'Name':['Alice', 'Bob', 'Charlie'], 'City':['Chicago', 'Boston', 'Dallas'],'Active':['N', 'N', 'Y']})

data = pd.DataFrame([
    {"Name":f"User {i}", "City": f"City {i}", "Active_Status": "Y" if i % 2 == 0 else "N"}
    for i in range(1, 101)
])

name_list = data["Name"].astype(str).tolist()

rows_per_page = 10
#total_pages = len(data) // rows_per_page + (1 if len(data) % rows_per_page > 0 else 0)

#if "current_page" not in st.session_state:
#    st.session_state.current_page = 0

#start_idx = st.session_state.current_page*rows_per_page
#end_idx = start_idx + rows_per_page
#paged_data = data.iloc[start_idx:end_idx]
paged_data = paginate_dataframe(data, rows_per_page)

edited_data = st.data_editor(paged_data, hide_index = True, key = "data_editor", disabled = True)

st.subheader("Select a Record to Edit:")
selected_name = st.selectbox("Search & Select a Row", name_list , index=0)

st.session_state.selected_index = data[data["Name"] == selected_name].index[0]
selected_index = st.session_state.selected_index

with st.form("edit form"):
    selected_name = st.text_input("Name", value=data.iloc[selected_index]["Name"])
    selected_city = st.text_input("City", value=data.iloc[selected_index]["City"])
    selected_status = st.selectbox("Active Status", ["Y","N"], index=["Y", "N"].index(data.iloc[selected_index]["Active_Status"]))
    submitted = st.form_submit_button("Save")
        

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
            
