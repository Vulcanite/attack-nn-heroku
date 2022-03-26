import streamlit as st
from multiapp import MultiApp
from apps import home, AttackRNN, triggered, glossary

st.set_page_config(layout="wide")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Attack on RNN", AttackRNN.app)
app.add_app("Triggered attack", triggered.app)
app.add_app("Glossary", glossary.app)


# The main app
app.run()