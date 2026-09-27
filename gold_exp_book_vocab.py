import streamlit as st

st.title("📚 Gold Experience Vocabulary Challenge")
st.write("ม.4 | Unit 3 - 5 (20 ข้อ)")

questions = [
    # Unit 3: Technology & Media
    {
        "question": "You need to ___ your photo to the website if you want to enter the contest.",
        "options": ["download", "upload", "delete", "search"],
        "answer": "upload"
    },
    {
        "question": "I forgot to save my document, and now the computer screen is completely ___.",
        "options": ["frozen", "online", "connected", "digital"],
        "answer": "frozen"
    },
    {
        "question": "Don't forget to ___ out of your social media account when using a public computer.",
        "options": ["log", "turn", "click", "switch"],
        "answer": "log"
    },
    {
        "question": "You can ___ on this link to visit the school's official page.",
        "options": ["press", "click", "type", "swipe"],
        "answer": "click"
    },
    {
        "question": "My phone battery is low, so I need to find a ___.",
        "options": ["charger", "keyboard", "screen", "headphone"],
        "answer": "charger"
    },
    {
        "question": "Scientists hope to ___ new technology to help clean the oceans.",
        "options": ["invent", "discover", "explore", "connect"],
        "answer": "invent"
    },
    {
        "question": "Make sure you install antivirus software to ___ your computer from viruses.",
        "options": ["protect", "damage", "repair", "replace"],
        "answer": "protect"
    },

    # Unit 4: Environment & Natural World
    {
        "question": "Global warming is causing temperatures around the world to ___.",
        "options": ["drop", "increase", "fall", "disappear"],
        "answer": "increase"
    },
    {
        "question": "We should reduce plastic waste to protect wild animals in their natural ___.",
        "options": ["habitat", "house", "society", "landscape"],
        "answer": "habitat"
    },
    {
        "question": "It is important to ___ paper, glass, and plastic to help the environment.",
        "options": ["reuse", "recycle", "throw", "pollute"],
        "answer": "recycle"
    },
    {
        "question": "Heavy rain caused a severe ___ that flooded many streets in the city.",
        "options": ["drought", "flood", "earthquake", "storm"],
        "answer": "flood"
    },
    {
        "question": "Many species of animals are in danger of becoming ___ if we don't protect them.",
        "options": ["extinct", "alive", "safe", "common"],
        "answer": "extinct"
    },
    {
        "question": "Air ___ is a serious problem in big cities with too many cars.",
        "options": ["pollution", "protection", "climate", "nature"],
        "answer": "pollution"
    },

    # Unit 5: Travel, Transport & Places
    {
        "question": "We arrived at the airport two hours early to ___ in our luggage.",
        "options": ["check", "take", "board", "get"],
        "answer": "check"
    },
    {
        "question": "Please keep your seatbelt fastened until the plane has landed at the ___.",
        "options": ["destination", "station", "stop", "platform"],
        "answer": "destination"
    },
    {
        "question": "The train was delayed, so we had to wait on the ___ for an hour.",
        "options": ["platform", "runway", "pavement", "gate"],
        "answer": "platform"
    },
    {
        "question": "We stayed at a cozy ___ near the lake during our vacation.",
        "options": ["campsite", "accommodation", "resort", "hotel"],
        "answer": "accommodation"
    },
    {
        "question": "Before traveling abroad, you must check if your ___ is still valid.",
        "options": ["ticket", "passport", "license", "card"],
        "answer": "passport"
    },
    {
        "question": "We booked a guided ___ to learn more about the history of the ancient ruins.",
        "options": ["trip", "tour", "journey", "voyage"],
        "answer": "tour"
    },
    {
        "question": "It's usually cheaper to travel during the off-peak ___.",
        "options": ["season", "time", "date", "holiday"],
        "answer": "season"
    }
]

# สร้างแบบฟอร์มตอบคำถาม
user_answers = {}
with st.form("vocab_quiz_form"):
    for idx, q in enumerate(questions, 1):
        st.subheader(f"ข้อที่ {idx}")
        user_answers[idx] = st.radio(
            q["question"], 
            q["options"], 
            key=f"vocab_{idx}",
            index=None
        )
        st.write("---")
    
    submitted = st.form_submit_button("ตรวจคำตอบ")

# ส่วนตรวจคำตอบและแสดงผล
if submitted:
    score = 0
    wrong_questions = []

    for idx, q in enumerate(questions, 1):
        user_ans = user_answers.get(idx)
        if user_ans == q["answer"]:
            score += 1
        else:
            wrong_questions.append({
                "no": idx,
                "question": q["question"],
                "user_ans": user_ans if user_ans else "ไม่ได้ตอบ",
                "correct_ans": q["answer"]
            })

    st.header("📊 สรุปผลคะแนน")
    st.success(f"คะแนนของคุณ: {score} / {len(questions)}")

    if score >= 18:
        st.balloons()
        st.write("🏆 ยอดเยี่ยมมาก! คลังคำศัพท์แน่นสุดๆ")
    elif score >= 15:
        st.write("🔥 ดีมาก! ทำได้เกิน 75%")
    elif score >= 10:
        st.write("👍 ผ่านเกณฑ์! ทบทวนคำศัพท์เพิ่มอีกนิดจะดีมาก")
    else:
        st.write("📚 ลองกลับไปทบทวนคำศัพท์ใน Unit 3-5 แล้วลองใหม่นะ")

    st.write("---")

    if wrong_questions:
        st.subheader("❌ ข้อที่คุณตอบผิด / ยังไม่ได้ตอบ:")
        for item in wrong_questions:
            st.error(f"**ข้อที่ {item['no']}:** {item['question']}")
            st.write(f"- **คำตอบของคุณ:** {item['user_ans']}")
            st.write(f"- **คำตอบที่ถูกต้อง:** :green[{item['correct_ans']}]")
            st.write("---")
    else:
        st.balloons()
        st.success("🎉 ยินดีด้วย! คุณตอบถูกต้องทุกข้อ")
