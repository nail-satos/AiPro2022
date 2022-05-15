# 必要なライブラリをインポートする
import streamlit as st

# testapp01(初級)
def app():
    st.title('簡易計算機')
    st.caption('値を入力')
    n1 = st.number_input(label='数値1', value=1)
    n2 = st.number_input(label='数値2', value=1)

    mess1 = '数値1＋数値2＝' + str(n1 + n2)
    mess2 = '数値1－数値2＝' + str(n1 - n2)
    mess3 = '数値1✕数値2＝' + str(n1 * n2)
    mess4 = '数値1÷数値2＝' + str(n1 / n2)

    st.caption('答え')
    st.write(mess1)
    st.write(mess2)
    st.write(mess3)
    st.write(mess4)
