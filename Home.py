import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(page_title='HOME')

with open ('./vdieos/beauty.mp4', 'rb') as f:
    video_bytes = f.read()
    st.video(video_bytes)

with open ('./vdieos/funny.mp4', 'rb') as f:
    video_bytes = f.read()
    st.video(video_bytes)
    
st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")