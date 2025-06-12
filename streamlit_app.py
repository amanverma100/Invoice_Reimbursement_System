import streamlit as st, requests, pandas as pd
from datetime import datetime

API = "http://localhost:8000"

st.set_page_config(page_title="Invoice Reimbursement System", layout="wide")
st.title("💰 Invoice Reimbursement System")

page = st.sidebar.selectbox("Page", ["Invoice Analysis", "Chat Assistant", "System Health"])

if page == "Invoice Analysis":
    policy = st.file_uploader("Policy PDF", type=['pdf'])
    invoices = st.file_uploader("Invoices ZIP", type=['zip'])
    name = st.text_input("Employee Name")
    if st.button("Analyze"):
        if policy and invoices and name:
            files = {"policy_file": policy, "invoices_zip": invoices}
            data = {"employee_name": name}
            r = requests.post(f"{API}/analyze-invoices", files=files, data=data)
            if r.status_code == 200:
                res = r.json()
                st.success(res["message"])
                for a in res["results"]:
                    with st.expander(a["invoice_filename"]):
                        st.metric("Status", a["reimbursement_status"])
                        st.metric("Total", f"₹{a['total_amount']}")
                        st.metric("Reimbursable", f"₹{a['reimbursable_amount']}")
                        st.write("Reason:", a["reason"])
                        if a["detailed_breakdown"]:
                            st.json(a["detailed_breakdown"])
            else:
                st.error(r.text)
        else:
            st.warning("Provide all inputs")

elif page == "Chat Assistant":
    if "history" not in st.session_state:
        st.session_state.history = []
    for m in st.session_state.history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if prompt := st.chat_input("Ask..."):
        st.session_state.history.append({"role":"user","content":prompt})
        r = requests.post(f"{API}/chat", json={"query":prompt,"chat_history":[{"role":x["role"],"content":x["content"]} for x in st.session_state.history[:-1]]})
        if r.status_code == 200:
            ans = r.json()["response"]
            st.session_state.history.append({"role":"assistant","content":ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error(r.text)

else:
    if st.button("Check API Health"):
        r = requests.get(f"{API}/health")
        if r.status_code == 200:
            st.success("API is healthy")
            st.json(r.json())
        else:
            st.error("API error")













