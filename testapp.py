# 必要なライブラリをインポートする
import streamlit as st

# 起動方法
# > streamlit run testapp.py

# サーバへのアクセス方法
# > Local URL: をブラウザで起動する

# 終了方法
# > (Ctrl) + (c)キー

# コードを改変したら、(Ctrl)+(C)で終了 → streamlit run app.py で再起動しましょう


###############################################################################
# 以降のコードは順次、レッスン単位でコメントアウトを解除しながら試行してください
###############################################################################

# Streamlitの基礎:レッスン1
# 文字を表示する
st.title('レッスン1')           # タイトル
st.header('レッスン1')          # ヘッダ
st.subheader('レッスン1')       # サブヘッダ
st.caption('レッスン1')         # キャプション
st.code('print("レッスン1"')    # ソースコード
st.write('レッスン1')           # 汎用的な出力
st.latex('S_{t+1}=S_{t}\exp(\mu \Delta_t+\sigma \sqrt{\Delta_t}\epsilon_t)')    # 数式（ラテック形式/tex:テフ）

# Streamlitの基礎:レッスン2
# 数値を入力する
n = st.number_input(label='数値を入力してください', value=7)

