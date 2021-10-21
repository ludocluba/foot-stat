import streamlit as st
import pandas as pd
import numpy as np
from db.read_db import read_players

st.title('Football stats')
st.write(read_players())