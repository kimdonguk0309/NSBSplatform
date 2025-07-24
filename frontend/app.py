import streamlit as st
import requests
from frontend.utils import generate_keypair

st.title("🛰️ NSBS 네트워크 공유 플랫폼")

tab1, tab2 = st.tabs(["공급자 등록", "수요자 연결"])

with tab1:
    st.subheader("공급자로 등록")
    name = st.text_input("이름")
    location = st.text_input("지역")
    endpoint = st.text_input("공개 Endpoint (예: 1.2.3.4:51820)")

    if st.button("등록"):
        response = requests.post("https://localhost:8000/register", json={
            "name": name,
            "location": location,
            "endpoint": endpoint
        }, verify=False)
        st.success(response.json())

with tab2:
    st.subheader("공급자 찾기 및 연결")
    providers = requests.get("https://localhost:8000/providers", verify=False).json()
    for p in providers:
        with st.expander(f"{p['name']} - {p['location']}"):
            if st.button(f"{p['name']}에게 연결 요청"):
                keys = generate_keypair()
                res = requests.post("https://localhost:8000/connect", json={
                    "client_private": keys["private_key"],
                    "provider_public": p["public_key"],
                    "endpoint": p["endpoint"]
                }, verify=False)
                st.code(res.json()["wg_config"], language="ini")
