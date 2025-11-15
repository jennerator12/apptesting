import streamlit as st
from transformers import pipeline

st.title("Humor Adapter")

options = ["Idiom", "Emoji", "Joke"] 
selection = st.segmented_control( "Type of Humor", options, selection_mode="single" ) 
st.markdown(f"You selected: {selection}.")

# Example dictionary
idioms_map = {
    "break a leg": {"Spanish": "¡Mucha suerte!", "French": "Merde!", "Korean": "행운을 빌어요!"},
    "piece of cake": {"Spanish": "Pan comido", "French": "C'est du gâteau", "Korean": "식은 죽 먹기"}
}

if selection:
    text = st.text_input(f"Enter your {selection.lower()}")
    language = st.selectbox("Adapt to language:", ["Spanish", "French", "Korean"])

    if st.button("Adapt Humor") and text.strip():
        adapted = idioms_map.get(text, {}).get(language, "No equivalent found!")
        st.success(adapted)
