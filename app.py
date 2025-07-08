import streamlit as st

# Check password from secrets.toml
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
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
    # Add your real logic here (image annotation, uploads, etc.)
