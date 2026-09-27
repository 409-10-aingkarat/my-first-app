import streamlit as st

st.title("🎮 English Grammar Quiz")
st.write("แบบทดสอบ Grammar 30 ข้อ")

questions = [
    # 1
    {
        "question": "I think I ___ study tonight.",
        "options": ["will", "am going to", "was", "had"],
        "answer": "will"
    },
    # 2
    {
        "question": "I ___ visit my grandmother tomorrow. I have already planned it.",
        "options": ["will", "am going to", "was", "had"],
        "answer": "am going to"
    },
    # 3
    {
        "question": "I ___ my friend at 6 p.m. tomorrow.",
        "options": ["meet", "am meeting", "met", "had met"],
        "answer": "am meeting"
    },
    # 4
    {
        "question": "The train ___ at 8 a.m. tomorrow.",
        "options": ["leaves", "will leaving", "left", "had left"],
        "answer": "leaves"
    },
    # 5
    {
        "question": "She ___ to school yesterday.",
        "options": ["go", "goes", "went", "will go"],
        "answer": "went"
    },
    # 6
    {
        "question": "I ___ dinner before I went to bed.",
        "options": ["eat", "ate", "had eaten", "will eat"],
        "answer": "had eaten"
    },
    # 7
    {
        "question": "If you heat ice, it ___.",
        "options": ["melts", "will melt", "would melt", "melted"],
        "answer": "melts"
    },
    # 8
    {
        "question": "If I study hard, I ___ pass the exam.",
        "options": ["would", "will", "had", "was"],
        "answer": "will"
    },
    # 9
    {
        "question": "If I were rich, I ___ a big house.",
        "options": ["buy", "will buy", "would buy", "bought"],
        "answer": "would buy"
    },
    # 10
    {
        "question": "If I had studied, I ___ the exam.",
        "options": ["will pass", "would pass", "would have passed", "passed"],
        "answer": "would have passed"
    },
    # 11
    {
        "question": "Which sentence uses Future Simple?",
        "options": [
            "I will call you.",
            "I am calling you.",
            "I called you.",
            "I had called you."
        ],
        "answer": "I will call you."
    },
    # 12
    {
        "question": "Which sentence uses 'be going to'?",
        "options": [
            "I will play football.",
            "I am going to play football.",
            "I played football.",
            "I had played football."
        ],
        "answer": "I am going to play football."
    },
    # 13
    {
        "question": "Which one is Present Continuous?",
        "options": [
            "I study.",
            "I studied.",
            "I am studying.",
            "I had studied."
        ],
        "answer": "I am studying."
    },
    # 14
    {
        "question": "Which one is Past Simple?",
        "options": [
            "I go.",
            "I will go.",
            "I went.",
            "I had gone."
        ],
        "answer": "I went."
    },
    # 15
    {
        "question": "Which one is Past Perfect?",
        "options": [
            "I eat.",
            "I ate.",
            "I will eat.",
            "I had eaten."
        ],
        "answer": "I had eaten."
    },
    # 16
    {
        "question": "Past Simple uses which verb form?",
        "options": ["V.1", "V.2", "V.3", "V.ing"],
        "answer": "V.2"
    },
    # 17
    {
        "question": "Past Perfect uses which structure?",
        "options": [
            "will + V.1",
            "V.2",
            "had + V.3",
            "am + V.ing"
        ],
        "answer": "had + V.3"
    },
    # 18
    {
        "question": "Zero Conditional is used for ___.",
        "options": [
            "general truths",
            "future plans",
            "past events",
            "appointments"
        ],
        "answer": "general truths"
    },
    # 19
    {
        "question": "First Conditional is mainly used for ___.",
        "options": [
            "unreal situations",
            "possible future situations",
            "past events",
            "general truths"
        ],
        "answer": "possible future situations"
    },
    # 20
    {
        "question": "Second Conditional is used for ___.",
        "options": [
            "imaginary situations",
            "timetables",
            "past facts",
            "scientific facts"
        ],
        "answer": "imaginary situations"
    },
    # 21
    {
        "question": "Third Conditional talks about ___.",
        "options": [
            "future plans",
            "general truths",
            "unreal past situations",
            "timetables"
        ],
        "answer": "unreal past situations"
    },
    # 22
    {
        "question": "If I ___ you, I would study harder.",
        "options": ["am", "was", "were", "will be"],
        "answer": "were"
    },
    # 23
    {
        "question": "If it rains tomorrow, I ___ at home.",
        "options": ["stay", "stayed", "will stay", "would stay"],
        "answer": "will stay"
    },
    # 24
    {
        "question": "If I had more money, I ___ a new phone.",
        "options": ["buy", "will buy", "would buy", "bought"],
        "answer": "would buy"
    },
    # 25
    {
        "question": "If she had studied, she ___ the test.",
        "options": [
            "will pass",
            "would pass",
            "would have passed",
            "passes"
        ],
        "answer": "would have passed"
    },
    # 26
    {
        "question": "Which word means 'ถ้าไม่'?",
        "options": ["unless", "because", "although", "while"],
        "answer": "unless"
    },
    # 27
    {
        "question": "Which phrase means 'เผื่อว่า'?",
        "options": ["unless", "in case", "because", "if not"],
        "answer": "in case"
    },
    # 28
    {
        "question": "Which sentence is Zero Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If you heat water, it boils.",
            "If I had studied, I would have passed."
        ],
        "answer": "If you heat water, it boils."
    },
    # 29
    {
        "question": "Which sentence is Second Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If you heat ice, it melts.",
            "If I had studied, I would have passed."
        ],
        "answer": "If I were rich, I would travel."
    },
    # 30
    {
        "question": "Which sentence is Third Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If you heat ice, it melts.",
            "If I had studied, I would have passed."
        ],
        "answer": "If I had studied, I would have passed."
    }
]

score = 0

for i, q in enumerate(questions):
    st.subheader(f"ข้อ {i + 1}")
    answer = st.radio(
        q["question"],
        q["options"],
        key=f"question_{i}"
    )

    if answer == q["answer"]:
        score += 1

if st.button("ตรวจคำตอบ"):
    st.success(f"คะแนนของคุณคือ {score}/30")

    if score >= 24:
        st.balloons()
        st.write("🎉 เก่งมาก!")
    elif score >= 18:
        st.write("👍 ทำได้ดี!")
    else:
        st.write("📚 ลองทบทวนอีกครั้ง!")
