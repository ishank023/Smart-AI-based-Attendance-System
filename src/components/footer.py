import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; justify-content:center; align-items:center; gap:6px;">
            <p style="font-weight:bold; color:white; margin:0;">Created by Ishank</p>
            <img src="{logo_url}" style="height:24px;" />
        </div>
    """, unsafe_allow_html=True)