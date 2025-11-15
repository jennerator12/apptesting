import streamlit as st
from transformers import pipeline

st.title("Humor Adapter")

options = ["Idiom", "Emoji", "Joke"] 
selection = st.segmented_control( "Type of Humor", options, selection_mode="single" ) 
st.markdown(f"You selected: {selection}.")


