import streamlit as st
import pandas as pd

from api.fast import root

st.write(root())

st.write('This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')

st.write(pd.DataFrame({"name":["Henry"],"age":[30]}))
