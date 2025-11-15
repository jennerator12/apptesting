import streamlit as st
from transformers import pipeline

st.title("Humor Adapter")

options = ["Idiom", "Emoji", "Joke"] 
selection = st.segmented_control( "Type of Humor", options, selection_mode="single" ) 
st.markdown(f"You selected: {selection}.")

# Idioms, emojis, and simple jokes with culturally equivalent phrases
humor_map = {
    # IDIOMS
    "break a leg": {
        "Spanish": "¡Mucha suerte!",
        "French": "Merde!",
        "Korean": "행운을 빌어요!"
    },
    "piece of cake": {
        "Spanish": "Pan comido",
        "French": "C'est du gâteau",
        "Korean": "식은 죽 먹기"
    },
    "hit the sack": {
        "Spanish": "Ir a la cama",
        "French": "Aller au lit",
        "Korean": "잠자러 가다"
    },
    "spill the beans": {
        "Spanish": "Revelar el secreto",
        "French": "Vendre la mèche",
        "Korean": "비밀을 누설하다"
    },
    "costs an arm and a leg": {
        "Spanish": "Cuesta un ojo de la cara",
        "French": "Coûter les yeux de la tête",
        "Korean": "엄청 비싸다"
    },
    
    # EMOJIS
    "😂": {
        "Spanish": "😂",
        "French": "😂",
        "Korean": "😂"
    },
    "👍": {
        "Spanish": "¡Genial! 👍",
        "French": "Super ! 👍",
        "Korean": "좋아요! 👍"
    },
    "🎉": {
        "Spanish": "¡Felicidades! 🎉",
        "French": "Félicitations ! 🎉",
        "Korean": "축하합니다! 🎉"
    },

    # JOKES (simple, family-friendly)
    "Why did the chicken cross the road?": {
        "Spanish": "¿Por qué cruzó el pollo la calle? Para llegar al otro lado.",
        "French": "Pourquoi le poulet a-t-il traversé la route ? Pour arriver de l'autre côté.",
        "Korean": "닭은 왜 길을 건넜을까? 반대편에 가기 위해서야."
    },
    "I told my computer I needed a break, and it said no problem.": {
        "Spanish": "Le dije a mi computadora que necesitaba un descanso, y dijo: 'Sin problema.'",
        "French": "J'ai dit à mon ordinateur que j'avais besoin d'une pause, et il a dit: 'Pas de problème.'",
        "Korean": "컴퓨터에게 쉬고 싶다고 했더니, 문제 없다고 하더라."
    },
    "Why don't scientists trust atoms?": {
        "Spanish": "¿Por qué los científicos no confían en los átomos? ¡Porque lo componen todo!",
        "French": "Pourquoi les scientifiques ne font-ils pas confiance aux atomes ? Parce qu'ils constituent tout !",
        "Korean": "과학자들은 왜 원자를 믿지 않을까? 모든 것을 이루고 있기 때문이야!"
    }
}


if selection:
    text = st.text_input(f"Enter your {selection.lower()}")
    language = st.selectbox("Adapt to language:", ["Spanish", "French", "Korean"])

    if st.button("Adapt Humor") and text.strip():
        adapted = idioms_map.get(text, {}).get(language, "No equivalent found!")
        st.success(adapted)
