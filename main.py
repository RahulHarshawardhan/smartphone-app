import streamlit as st
from dbhelp import DB

db = DB()

st.sidebar.title('Smart Phone Analysis')

brand_name = db.phone_brand()
option = st.sidebar.selectbox('select brand name', brand_name)

models = db.model_selection(option)
option1 =st.sidebar.selectbox('Select Model Name', models)

if st.sidebar.button("Search Details"):
    results = db.fetch_features(option, option1)
    st.table(results)








