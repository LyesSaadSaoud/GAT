import streamlit as st
import os

# Check password from environment variable (Render-compatible)
def check_password():
    def password_entered():
        correct_password = os.environ.get("password", "")  # ✅ Render will pass this if set in environment variables
        if st.session_state["password"] == correct_password:
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        st.error("❌ Incorrect password.")
        return False
    else:
        return True

if check_password():
    st.title("🦅 Generalized Annotation Tool (GAT)")
    st.write("Welcome to the Streamlit version of the GAT app.")
    # Add your annotation logic here
