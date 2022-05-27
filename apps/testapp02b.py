# 必要なライブラリをインポートする
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():

     # 画像ファイルをアップロードする
     uploaded_file=st.file_uploader("ファイルアップロード", type='png')

     # アップロードの有無を判定する条件式
     if uploaded_file is not None:

          # アップロードされた画像を開く
          image=Image.open(uploaded_file)

          # Image.openで開くとRGB + α(透過度)の4次元 → RGBの3次元データに変換する
          img_rgb = np.array(image.convert('RGB'))

          # 画像を表示する（use_column_width：画像サイズ（横幅）を自動調整）
          st.image(img_rgb, caption = 'サムネイル画像',use_column_width = True)


     ### ここから(課題:初級)　###

     # ボタンが押下された場合の処理...
     if st.button('初級'):

          # 画像の認識結果を表示する（未完成）
          if(img_rgb[15, 15 ,0] >= 200 and img_rgb[15, 15 ,1] <= 128):
               st.title('この画像はリンゴです！')
          else:
               st.title('この画像はバナナです！')

     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')


     ### ここから(課題:中級)　###

     # ボタンが押下された場合の処理...
     if st.button('中級'):
          sampling_num = 5
          sampling_height = int((img_rgb.shape[0] - 1) / sampling_num)
          sampling_width = int((img_rgb.shape[1] - 1) / sampling_num)

          apple_num = 0
          banana_num = 0

          for i in range(sampling_num + 1):
               for j in range(sampling_num + 1):
                    if(img_rgb[i * sampling_height, j * sampling_width ,0] >= 180 and img_rgb[i * sampling_height, j * sampling_width ,1] <= 128):
                         apple_num = apple_num + 1
                    elif(img_rgb[i * sampling_height, j * sampling_width ,0] >= 180 and img_rgb[i * sampling_height, j * sampling_width ,1] >= 150 and img_rgb[i * sampling_height, j * sampling_width ,2] <= 128):
                         banana_num = banana_num + 1

          if(apple_num == 0 and banana_num == 0):
               st.title('この画像はリンゴでもバナナでも無い気がします！')
          elif(apple_num >= banana_num):
               st.title('この画像はリンゴです！')
          else:
               st.title('この画像はバナナです！')

     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')

     ### ここから(課題:上級)　###

     # ボタンが押下された場合の処理...
     if st.button('上級'):
          sampling_num = 5
          sampling_height = int((img_rgb.shape[0] - 1) / sampling_num)
          sampling_width = int((img_rgb.shape[1] - 1) / sampling_num)

          apple_num = 0
          banana_num = 0

          for i in range(sampling_num + 1):
               for j in range(sampling_num + 1):
                    if(img_rgb[i * sampling_height, j * sampling_width ,0] >= 180 and img_rgb[i * sampling_height, j * sampling_width ,1] <= 128):
                         apple_num = apple_num + 1
                    elif(img_rgb[i * sampling_height, j * sampling_width ,0] >= 180 and img_rgb[i * sampling_height, j * sampling_width ,1] >= 150 and img_rgb[i * sampling_height, j * sampling_width ,2] <= 128):
                         banana_num = banana_num + 1

          if(apple_num == 0 and banana_num == 0):
               st.title('この画像はリンゴでもバナナでも無い気がします！')
          elif(apple_num >= banana_num):
               st.title('この画像はリンゴです！')
          else:
               st.title('この画像はバナナです！')

     # ボタンが押下される前の処理...
     else:
          st.write('画像をアップロードしてから、ボタンを押してください')

