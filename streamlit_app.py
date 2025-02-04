import streamlit as st
import pandas as pd

st.title("🎈 Checkbox Toggle Test")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'id':[1,2,3], 'active':[False, False, False]})
column_config = {'active':st.column_config.CheckboxColumn('Active Status', disabled=st.session_state.df['active'].tolist())}

st.write("**Before Edit:**", st.session_state.df['active'].tolist())
edited_df = st.data_editor(st.session_state.df, column_config = column_config, key = "unique_editor_key", use_container_width = True)

if not edited_df.equals(st.session_state.df):
    st.session_state.df = edited_df
    st.rerun()

st.write("**After Edit:**", st.session_state.df['active'].tolist())
