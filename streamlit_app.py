import streamlit as st

st.title("🦋 Welcome to My Streamlit App!")
st.subheader("Built with love, logic, and creativity 💡")

user_input = st.text_input("Ask me anything:")
if user_input:
    st.write(f"You said: {user_input}")