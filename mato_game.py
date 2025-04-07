import streamlit as st
import random

st.set_page_config(page_title="的あてゲーム", page_icon="🎯")

st.title("的あてゲーム")

# セッション変数で状態管理
if "target_x" not in st.session_state:
    st.session_state.target_x = random.randint(1, 5)
    st.session_state.score = 0
    st.session_state.shots = 0

st.write("的の位置：1〜5 のどこかに出現します！")
st.write("どこを狙う？")

# プレイヤーの選択
choice = st.radio("狙う位置を選んでください", [1, 2, 3, 4, 5], horizontal=True)

if st.button("撃つ！"):
    st.session_state.shots += 1
    if choice == st.session_state.target_x:
        st.success("命中！スコア +1")
        st.session_state.score += 1
    else:
        st.warning(f"はずれ…（正解は {st.session_state.target_x}）")

    # 次のターゲット
    st.session_state.target_x = random.randint(1, 5)

# スコア表示
st.metric(label="スコア", value=st.session_state.score)
st.metric(label="ショット数", value=st.session_state.shots)

# リセット
if st.button("リセット"):
    st.session_state.target_x = random.randint(1, 5)
    st.session_state.score = 0
    st.session_state.shots = 0
