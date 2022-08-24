# ! python3
#import all the necessary libraries
import streamlit as st 
from gtts import gTTS
from googletrans import Translator
from PIL import Image

st.title("Once upon a time")
st.header("Analyze Gimm`s fairy tales")

#add sidebar with some basic information about the app
#add logo
logo = Image.open(r"
