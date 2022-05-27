# 必要なライブラリをインポートする
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


# 画像のRGBをそれぞれ足してRGBの割合を計算する関数
def rgb_rate_calculation(img_rgb):
     """RGBの割合を計算する関数
     
     グレーや白のような背景色は除外して計算している。

     --------------------------------------------------
     args:
          img_rgb: 画像のRGBデータ

     --------------------------------------------------
     return:
          red_rate: 赤の割合
          green_rate: 緑の割合
          blue_rate: 青の割合

          赤、緑、青の順にタプルで返される

     --------------------------------------------------
     """
     red_count = 0
     green_count = 0   
     blue_count = 0
     for x_rgb in img_rgb:
          for rgb in x_rgb:
               if not(rgb[0] > 150 and rgb[1] > 150 and rgb[2] > 150):
                    red_count += rgb[0]
                    green_count += rgb[1]
                    blue_count += rgb[2]
                    
     # 各色が全体を占める割合を計算
     red_rate = red_count / (red_count + green_count + blue_count)
     green_rate = green_count / (red_count + green_count + blue_count)
     blue_rate = blue_count / (red_count + green_count + blue_count)

     # 各色が全体を占める割合を返す
     return red_rate, green_rate, blue_rate



# RGBの割合からどんな画像なのかを判定する関数
def image_judgement(red_rate, green_rate, blue_rate):
     """RGBの割合からどんな画像なのかを判定する関数

     全ての難易度で判定出来るように閾値を設定済み。

     --------------------------------------------------
     args:
          red_rate: 赤の割合
          green_rate: 緑の割合
          blue_rate: 青の割合

          赤、緑、青の順に渡す
     
     --------------------------------------------------
     return:
          image_name: 画像の名前

          りんごorバナナが文字列で返される。
          どちらとも判別できない場合はその他が文字列で返される

     --------------------------------------------------
     """
     if red_rate > 0.5 and green_rate < 0.3 and blue_rate < 0.3:
          return "りんご" 

     elif red_rate > 0.35 and green_rate > 0.35 and blue_rate < 0.25:
          return "バナナ"
     else:
          return "その他"



def app():

     # 画像ファイルをアップロードする
     uploaded_file=st.file_uploader("ファイルアップロード", type=['png', 'jpg', 'jpeg'])

     # アップロードの有無を判定する条件式
     if uploaded_file is not None:

          # アップロードされた画像を開く
          image=Image.open(uploaded_file)

          # Image.openで開くとRGB + α(透過度)の4次元 → RGBの3次元データに変換する
          img_rgb = np.array(image.convert('RGB'))

          print(img_rgb.shape)

          # 画像を表示する（use_column_width：画像サイズ（横幅）を自動調整）
          st.image(img_rgb, caption = 'サムネイル画像',use_column_width = True)


     ### ここから(課題:初級)　###

     # ボタンが押下された場合の処理...
     if st.button('初級'):

          # RGBの割合を計算する
          rgb_rate = rgb_rate_calculation(img_rgb)

          red_rate = rgb_rate[0]
          green_rate = rgb_rate[1]
          blue_rate = rgb_rate[2]
          
          # 割合表示用
          # st.write("Red : " + str(red_rate))
          # st.write("Green : " + str(red_rate))
          # st.write("Blue : " + str(blue_rate))

          st.write("判定結果：" + image_judgement(red_rate, green_rate, blue_rate))

     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')



               
     ### ここから(課題:中級)　###

     # ボタンが押下された場合の処理...
     if st.button('中級'):
          st.write('中級')
          
          # RGBの割合を計算する
          rgb_rate = rgb_rate_calculation(img_rgb)

          red_rate = rgb_rate[0]
          green_rate = rgb_rate[1]
          blue_rate = rgb_rate[2]

          st.write("判定結果：" + image_judgement(red_rate, green_rate, blue_rate))


     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')


     ### ここから(課題:上級)　###

     # ボタンが押下された場合の処理...
     if st.button('上級'):

          # RGBの割合を計算する
          rgb_rate = rgb_rate_calculation(img_rgb)

          red_rate = rgb_rate[0]
          green_rate = rgb_rate[1]
          blue_rate = rgb_rate[2]
          
          # 上級調整用の割合表示
          st.write("Red : " + str(red_rate))
          st.write("Green : " + str(green_rate))
          st.write("Blue : " + str(blue_rate))

          # 結果出力
          st.write("判定結果：" + image_judgement(red_rate, green_rate, blue_rate))


     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')

