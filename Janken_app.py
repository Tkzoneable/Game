import streamlit as st
import random

st.title("じゃんけんゲーム")

choices = ["グー", "チョキ", "パー"]
user_choice = st.radio("あなたの手を選んでください", choices)

if st.button("勝負！"):
    cpu_choice = random.choice(choices)
    st.write(f"相手の手: {cpu_choice}")

    if user_choice == cpu_choice:
        st.success("あいこ！")
    elif (
        (user_choice == "グー" and cpu_choice == "チョキ") or
        (user_choice == "チョキ" and cpu_choice == "パー") or
        (user_choice == "パー" and cpu_choice == "グー")
    ):
        st.success("あなたの勝ち！")
    else:
        st.error("あなたの負け…")
