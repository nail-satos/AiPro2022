import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats
from apps import testapp01c, testapp01b, testapp01a, testapp01x

app = MultiApp() 

# app.add_app("Home", home.app)
# app.add_app("Data Stats", data_stats.app) 
app.add_app("testapp01(課題1-初級)", testapp01c.app) 
app.add_app("testapp01(課題1-中級)", testapp01b.app) 
app.add_app("testapp01(課題1-上級)", testapp01a.app) 
app.add_app("testapp01(課題2-初/中/上級)", testapp01x.app) 

app.run()