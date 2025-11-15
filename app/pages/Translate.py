import streamlit as st
from transformers import pipeline

st.title("Humor Adapter")

options = ["Idiom", "Emoji", "Joke"] 
selection = st.segmented_control( "Type of Humor", options, selection_mode="single" ) 
st.markdown(f"You selected: {selection}.")

if selection:
    text = st.text_input(f"Enter your {selection.lower()}")
    language = st.selectbox("Adapt to language:", ["Spanish", "French", "Korean"])

    if st.button("Adapt Humor") and text.strip():
        try:
            # Hugging Face text generation pipeline
            generator = pipeline("text-generation", model="gpt2-medium")
            raw = generator(
                f"Rewrite this {selection.lower()} in {language} and keep it funny: {text}",
                max_new_tokens=50,
                truncation=True
            )[0]["generated_text"]
            adapted = raw.split("\n")[0].strip()
            st.success(adapted)
        except Exception as e:
            st.error(f"Error generating text: {e}")
