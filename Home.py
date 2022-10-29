import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(page_title='HOME')

video_file = open('./vdieos/726.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)