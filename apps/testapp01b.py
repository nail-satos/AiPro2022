# 必要なライブラリをインポートする
import streamlit as st

# testapp01(中級)
def app():
    st.title('簡易計算機(中級)')
    st.caption('値を入力')
    n1 = st.number_input(label='数値1', value=1)
    n2 = st.number_input(label='数値2', value=1)

    selected_item = st.radio('演算の種類', ['加算', '減算', '乗算', '除算'])

    if selected_item == '加算':
        mess = '数値1＋数値2＝' + str(n1 + n2)

    if selected_item == '減算':
        mess = '数値1－数値2＝' + str(n1 - n2)

    if selected_item == '乗算':
        mess = '数値1✕数値2＝' + str(n1 * n2)
        
    if selected_item == '除算':
        mess = '数値1÷数値2＝' + str(n1 / n2)


    st.caption('答え')
    st.write(mess)
