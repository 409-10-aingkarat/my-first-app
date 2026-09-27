import streamlit as st

st.title("🎮 English Grammar Challenge")
st.write("ระดับชั้น ม.4 | 30 ข้อ")

questions = [
    {
        "question": "Look at those dark clouds! It ___ rain.",
        "options": [
            "will",
            "is going to",
            "is raining",
            "rains"
        ],
        "answer": "is going to"
    },
    {
        "question": "I think people ___ live on Mars one day.",
        "options": [
            "are going to",
            "will",
            "are living",
            "lived"
        ],
        "answer": "will"
    },
    {
        "question": "We ___ our teacher at 9 a.m. tomorrow.",
        "options": [
            "meet",
            "met",
            "are meeting",
            "will meeting"
        ],
        "answer": "are meeting"
    },
    {
        "question": "The English class ___ at 8:30 tomorrow morning.",
        "options": [
            "starts",
            "is starting",
            "started",
            "will started"
        ],
        "answer": "starts"
    },
    {
        "question": "She ___ to Bangkok last weekend.",
        "options": [
            "goes",
            "has gone",
            "went",
            "had gone"
        ],
        "answer": "went"
    },
    {
        "question": "When I arrived, the movie ___.",
        "options": [
            "already started",
            "had already started",
            "has already started",
            "will start"
        ],
        "answer": "had already started"
    },
    {
        "question": "By the time we got there, they ___ dinner.",
        "options": [
            "finished",
            "had finished",
            "finish",
            "will finish"
        ],
        "answer": "had finished"
    },
    {
        "question": "If you heat water to 100°C, it ___.",
        "options": [
            "will boil",
            "would boil",
            "boils",
            "boiled"
        ],
        "answer": "boils"
    },
    {
        "question": "If I study harder, I ___ better grades.",
        "options": [
            "get",
            "would get",
            "will get",
            "got"
        ],
        "answer": "will get"
    },
    {
        "question": "If she practices every day, she ___ improve.",
        "options": [
            "would",
            "will",
            "had",
            "was"
        ],
        "answer": "will"
    },
    {
        "question": "If I ___ enough money, I would buy a new laptop.",
        "options": [
            "have",
            "had",
            "will have",
            "had had"
        ],
        "answer": "had"
    },
    {
        "question": "If I were you, I ___ apologize to her.",
        "options": [
            "will",
            "would",
            "am",
            "had"
        ],
        "answer": "would"
    },
    {
        "question": "If he worked harder, he ___ the exam.",
        "options": [
            "will pass",
            "would pass",
            "passes",
            "had passed"
        ],
        "answer": "would pass"
    },
    {
        "question": "If I had known about the test, I ___ harder.",
        "options": [
            "would study",
            "will study",
            "would have studied",
            "study"
        ],
        "answer": "would have studied"
    },
    {
        "question": "If she had left earlier, she ___ the bus.",
        "options": [
            "would catch",
            "will catch",
            "would have caught",
            "catches"
        ],
        "answer": "would have caught"
    },
    {
        "question": "If you don't hurry, you ___ late.",
        "options": [
            "are",
            "were",
            "will be",
            "would be"
        ],
        "answer": "will be"
    },
    {
        "question": "Unless you study, you ___ pass the exam.",
        "options": [
            "will",
            "won't",
            "would",
            "had"
        ],
        "answer": "won't"
    },
    {
        "question": "Take an umbrella ___ it rains later.",
        "options": [
            "unless",
            "in case",
            "although",
            "because"
        ],
        "answer": "in case"
    },
    {
        "question": "I won't go outside ___ the rain stops.",
        "options": [
            "in case",
            "unless",
            "because",
            "when"
        ],
        "answer": "unless"
    },
    {
        "question": "Which sentence is Zero Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If you mix blue and yellow, you get green.",
            "If I had studied, I would have passed."
        ],
        "answer": "If you mix blue and yellow, you get green."
    },
    {
        "question": "Which sentence is First Conditional?",
        "options": [
            "If I were you, I would leave.",
            "If it rains, I will stay home.",
            "If you heat ice, it melts.",
            "If I had known, I would have helped."
        ],
        "answer": "If it rains, I will stay home."
    },
    {
        "question": "Which sentence is Second Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If water freezes, it becomes ice.",
            "If I had studied, I would have passed."
        ],
        "answer": "If I were rich, I would travel."
    },
    {
        "question": "Which sentence is Third Conditional?",
        "options": [
            "If I study, I will pass.",
            "If I were rich, I would travel.",
            "If I had studied, I would have passed.",
            "If I study every day, I get better."
        ],
        "answer": "If I had studied, I would have passed."
    },
    {
        "question": "Which sentence shows a planned future arrangement?",
        "options": [
            "I will visit him.",
            "I am visiting him tomorrow.",
            "I visited him yesterday.",
            "I had visited him."
        ],
        "answer": "I am visiting him tomorrow."
    },
    {
        "question": "Which sentence refers to a timetable?",
        "options": [
            "The train leaves at 7 p.m.",
            "The train will leave at 7 p.m.",
            "The train is going to leave.",
            "The train left at 7 p.m."
        ],
        "answer": "The train leaves at 7 p.m."
    },
    {
        "question": "Which sentence expresses a spontaneous decision?",
        "options": [
            "I am going to help you.",
            "I will help you.",
            "I am helping you tomorrow.",
            "I helped you."
        ],
        "answer": "I will help you."
    },
    {
        "question": "I ___ my homework before my friends arrived.",
        "options": [
            "finished",
            "had finished",
            "finish",
            "will finish"
        ],
        "answer": "had finished"
    },
    {
        "question": "If I ___ more careful, I wouldn't make so many mistakes.",
        "options": [
            "am",
            "were",
            "will be",
            "had been"
        ],
        "answer": "were"
    },
    {
        "question": "If they had practiced more, they ___ the competition.",
        "options": [
            "would win",
            "will win",
            "would have won",
            "won"
        ],
        "answer": "would have won"
    },
    {
        "question": "If you don't save your work, you ___ lose it.",
        "options": [
            "would",
            "will",
            "had",
            "were"
        ],
        "answer": "will"
    }
]

score = 0

for i, q in enumerate(questions):
    st.subheader(f"ข้อ {i + 1}")

    answer = st.radio(
        q["question"],
        q["options"],
        index=None,
        key=f"question_{i}"
    )

    if answer is not None and answer == q["answer"]:
        score += 1


if st.button("ตรวจคำตอบ"):
    unanswered = sum(
        1 for i in range(len(questions))
        if st.session_state.get(f"question_{i}") is None
    )

    if unanswered > 0:
        st.warning(f"ยังไม่ได้ตอบ {unanswered} ข้อ")
    else:
        st.success(f"🎉 คะแนนของคุณ: {score}/30")

        if score >= 27:
            st.balloons()
            st.write("🏆 ยอดเยี่ยมมาก!")
        elif score >= 24:
            st.write("🔥 ดีมาก!")
        elif score >= 18:
            st.write("👍 ผ่าน! แต่ยังทบทวนเพิ่มได้")
        else:
            st.write("📚 ลองทบทวน Grammar แล้วเล่นใหม่")
