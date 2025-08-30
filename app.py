import streamlit as st
import json
creds_info = json.loads(st.secrets["gcp_service_account"]["json"])
st.write(creds_info["private_key"][:50])  # só para conferir que está correto