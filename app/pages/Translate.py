import streamlit as st
st.title("Humor Adapter")

options = ["Idiom", "Emoji", "Joke", "Pun", "Saying"] 
selection = st.segmented_control( "Type of Humor", options, selection_mode="single" ) 
st.markdown(f"You selected: {selection}.")

# All keys are lowercase for case-insensitive lookup
humor_map = {
    # ----------------- IDIOMS -----------------
    "break a leg": {
        "Spanish": "¡Mucha suerte!",
        "French": "Merde!",
        "Korean": "행운을 빌어요!",
        "German": "Hals- und Beinbruch!",
        "Japanese": "頑張って！",
        "Chinese": "祝你好运！"
    },
    "piece of cake": {
        "Spanish": "Pan comido",
        "French": "C'est du gâteau",
        "Korean": "식은 죽 먹기",
        "German": "Kinderspiel",
        "Japanese": "朝飯前",
        "Chinese": "小菜一碟"
    },
    "hit the sack": {
        "Spanish": "Ir a la cama",
        "French": "Aller au lit",
        "Korean": "잠자러 가다",
        "German": "Ins Bett gehen",
        "Japanese": "寝る",
        "Chinese": "上床睡觉"
    },
    "spill the beans": {
        "Spanish": "Revelar el secreto",
        "French": "Vendre la mèche",
        "Korean": "비밀을 누설하다",
        "German": "Die Bohnen ausplaudern",
        "Japanese": "秘密を漏らす",
        "Chinese": "泄露秘密"
    },
    "costs an arm and a leg": {
        "Spanish": "Cuesta un ojo de la cara",
        "French": "Coûter les yeux de la tête",
        "Korean": "엄청 비싸다",
        "German": "Ein Vermögen kosten",
        "Japanese": "すごく高い",
        "Chinese": "非常昂贵"
    },
    "let the cat out of the bag": {
        "Spanish": "Revelar el secreto",
        "French": "Vendre la mèche",
        "Korean": "비밀을 누설하다",
        "German": "Die Katze aus dem Sack lassen",
        "Japanese": "秘密を漏らす",
        "Chinese": "泄露秘密"
    },
    "the ball is in your court": {
        "Spanish": "Te toca a ti",
        "French": "La balle est dans ton camp",
        "Korean": "네 차례야",
        "German": "Der Ball liegt bei dir",
        "Japanese": "次はあなたの番です",
        "Chinese": "轮到你了"
    },
    "burn the midnight oil": {
        "Spanish": "Quemar el aceite de medianoche",
        "French": "Brûler l'huile de minuit",
        "Korean": "밤늦게까지 일하다",
        "German": "Bis spät arbeiten",
        "Japanese": "夜遅くまで働く",
        "Chinese": "熬夜工作"
    },

    # ----------------- EMOJIS -----------------
    "😂": {
        "Spanish": "😂",
        "French": "😂",
        "Korean": "😂",
        "German": "😂",
        "Japanese": "😂",
        "Chinese": "😂"
    },
    "👍": {
        "Spanish": "¡Genial! 👍",
        "French": "Super ! 👍",
        "Korean": "좋아요! 👍",
        "German": "Super! 👍",
        "Japanese": "いいね！👍",
        "Chinese": "太棒了！👍"
    },
    "🎉": {
        "Spanish": "¡Felicidades! 🎉",
        "French": "Félicitations ! 🎉",
        "Korean": "축하합니다! 🎉",
        "German": "Herzlichen Glückwunsch! 🎉",
        "Japanese": "おめでとう！🎉",
        "Chinese": "恭喜！🎉"
    },
    "❤️": {
        "Spanish": "¡Te quiero! ❤️",
        "French": "Je t'aime ! ❤️",
        "Korean": "사랑해 ❤️",
        "German": "Ich liebe dich ❤️",
        "Japanese": "愛してる ❤️",
        "Chinese": "我爱你 ❤️"
    },
    "💡": {
        "Spanish": "¡Idea brillante! 💡",
        "French": "Bonne idée ! 💡",
        "Korean": "좋은 아이디어 💡",
        "German": "Tolle Idee 💡",
        "Japanese": "いいアイデア 💡",
        "Chinese": "好主意 💡"
    },

    # ----------------- JOKES -----------------
    "why did the chicken cross the road?": {
        "Spanish": "¿Por qué cruzó el pollo la calle? Para llegar al otro lado.",
        "French": "Pourquoi le poulet a-t-il traversé la route ? Pour arriver de l'autre côté.",
        "Korean": "닭은 왜 길을 건넜을까? 반대편에 가기 위해서야.",
        "German": "Warum hat das Huhn die Straße überquert? Um auf die andere Seite zu kommen.",
        "Japanese": "なぜニワトリは道を渡ったの？向こう側に行くため。",
        "Chinese": "鸡为什么过马路？为了到另一边。"
    },
    "i told my computer i needed a break, and it said no problem.": {
        "Spanish": "Le dije a mi computadora que necesitaba un descanso, y dijo: 'Sin problema.'",
        "French": "J'ai dit à mon ordinateur que j'avais besoin d'une pause, et il a dit: 'Pas de problème.'",
        "Korean": "컴퓨터에게 쉬고 싶다고 했더니, 문제 없다고 하더라.",
        "German": "Ich sagte meinem Computer, dass ich eine Pause brauche, und er sagte: 'Kein Problem.'",
        "Japanese": "コンピューターに休憩が必要だと言ったら、『問題ない』と言われた。",
        "Chinese": "我告诉电脑我需要休息，它说没问题。"
    },
    "why don't scientists trust atoms?": {
        "Spanish": "¿Por qué los científicos no confían en los átomos? ¡Porque lo componen todo!",
        "French": "Pourquoi les scientifiques ne font-ils pas confiance aux atomes ? Parce qu'ils constituent tout !",
        "Korean": "과학자들은 왜 원자를 믿지 않을까? 모든 것을 이루고 있기 때문이야!",
        "German": "Warum vertrauen Wissenschaftler Atomen nicht? Weil sie alles ausmachen!",
        "Japanese": "なぜ科学者は原子を信用しないの？すべてを作っているから。",
        "Chinese": "科学家为什么不相信原子？因为它们组成了一切！"
    },
    "i'm reading a book about anti-gravity, it's impossible to put down.": {
        "Spanish": "Estoy leyendo un libro sobre antigravedad, es imposible dejarlo.",
        "French": "Je lis un livre sur l'anti-gravité, il est impossible à poser.",
        "Korean": "반중력에 관한 책을 읽고 있는데, 내려놓을 수가 없어요.",
        "German": "Ich lese ein Buch über Antigravitation, es ist unmöglich wegzulegen.",
        "Japanese": "反重力についての本を読んでいるけど、手放せない。",
        "Chinese": "我在读一本关于反重力的书，根本放不下。"
    },

    # ----------------- PUNS / WORDPLAY -----------------
    "time flies like an arrow; fruit flies like a banana": {
        "Spanish": "El tiempo vuela como una flecha; las moscas de la fruta como un plátano",
        "French": "Le temps file comme une flèche ; les mouches des fruits comme une banane",
        "Korean": "시간은 화살처럼 빠르게 간다; 과일 파리는 바나나처럼",
        "German": "Die Zeit vergeht wie ein Pfeil; Fruchtfliegen wie eine Banane",
        "Japanese": "時間は矢のように飛ぶ；果物のハエはバナナのように",
        "Chinese": "时间像箭一样飞逝；果蝇像香蕉一样飞。"
    },

    # ----------------- PROVERBS / SAYINGS -----------------
    "the early bird catches the worm": {
        "Spanish": "Al que madruga, Dios le ayuda",
        "French": "Le monde appartient à ceux qui se lèvent tôt",
        "Korean": "일찍 일어나는 새가 벌레를 잡는다",
        "German": "Morgenstund hat Gold im Mund",
        "Japanese": "早起きは三文の徳",
        "Chinese": "早起的鸟儿有虫吃"
    },
    "actions speak louder than words": {
        "Spanish": "Las acciones hablan más que las palabras",
        "French": "Les actions parlent plus que les mots",
        "Korean": "행동이 말보다 중요하다",
        "German": "Taten sagen mehr als Worte",
        "Japanese": "行動は言葉よりも雄弁である",
        "Chinese": "行动胜于言辞"
    },
    "practice makes perfect": {
        "Spanish": "La práctica hace al maestro",
        "French": "C'est en forgeant qu'on devient forgeron",
        "Korean": "연습이 완벽을 만든다",
        "German": "Übung macht den Meister",
        "Japanese": "習うより慣れろ",
        "Chinese": "熟能生巧"
    }
}


# Separate the keys by category for the dropdowns
idioms = [
    "break a leg",
    "piece of cake",
    "hit the sack",
    "spill the beans",
    "costs an arm and a leg",
    "let the cat out of the bag",
    "the ball is in your court",
    "burn the midnight oil"
]

emojis = ["😂", "👍", "🎉", "❤️", "💡"]

jokes = [
    "why did the chicken cross the road?",
    "i told my computer i needed a break, and it said no problem.",
    "why don't scientists trust atoms?",
    "i'm reading a book about anti-gravity, it's impossible to put down."
]

puns = ["time flies like an arrow; fruit flies like a banana"]

sayings = [
    "the early bird catches the worm",
    "actions speak louder than words",
    "practice makes perfect"
]

# Combine into a dict for easy lookup
category_map = {
    "Idiom": idioms,
    "Emoji": emojis,
    "Joke": jokes,
    "Pun": puns,
    "Saying": sayings
}

if selection:
    # Dropdown of predefined phrases
    predefined_choice = st.selectbox("Select a predefined phrase:", [""] + category_map[selection])

    # Or type a new phrase
    custom_text = st.text_input("Or type your own phrase:")

    # Decide which one to use
    if custom_text.strip():
        phrase = custom_text.strip()
        is_custom = True
    else:
        phrase = predefined_choice
        is_custom = False

    # Language selection
    language = st.selectbox(
        "Adapt to language:",
        ["Spanish", "French", "Korean", "German", "Japanese", "Chinese"]
    )

    if st.button("Adapt Humor") and phrase:
        # If phrase is in dataset, return the predefined translation
        key = phrase.lower()
        if not is_custom and key in humor_map:
            adapted = humor_map[key].get(language, "No equivalent found!")
            st.success(adapted)
        else:
            # If custom, call a free AI model to generate a similar phrase
            st.info("Looking for a culturally similar phrase...")
            
            try:
                from transformers import pipeline

                # Small, free CPU-friendly model for text generation
                generator = pipeline("text-generation", model="distilgpt2", device=-1)

                prompt = f"Find a culturally equivalent {selection.lower()} in {language} for this English phrase: '{phrase}'"
                
                result = generator(prompt, max_new_tokens=50, truncation=True)[0]["generated_text"]
                
                # Postprocess: take the part after the prompt
                adapted = result.replace(prompt, "").strip().split("\n")[0]
                
                st.success(adapted)
            except Exception as e:
                st.error(f"Error generating AI phrase: {e}")