import streamlit as st
import random

st.set_page_config(
    page_title="Mood Mixer",
    page_icon="🌈",
    layout="centered"
)

# Simple styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e8f4ff, #f7eaff);
    }

    h1 {
        text-align: center;
        color: #4b4b6b;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
    }

    .result {
        background: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

st.title("🌈 Mood Mixer")
st.markdown(
    '<p class="subtitle">Pick your mood and discover your vibe ✨</p>',
    unsafe_allow_html=True
)

moods = {
    "😊 Happy": (
        "You're feeling good today!",
        "🎵 Put on your favourite song"
    ),
    "😴 Tired": (
        "You might need a little break.",
        "💧 Grab some water and relax"
    ),
    "😎 Confident": (
        "You've got this!",
        "💪 Do something you've been putting off"
    ),
    "😕 Meh": (
        "Some days are just meh.",
        "🍿 Watch something funny"
    ),
    "🤩 Excited": (
        "Your energy is HIGH!",
        "🎨 Try something creative"
    )
}

choice = st.selectbox(
    "How are you feeling?",
    list(moods.keys())
)

if st.button("✨ Mix My Mood"):
    message, activity = moods[choice]
    vibe = random.randint(1, 100)

    st.markdown(
        f"""
        <div class="result">
            <h2>{choice}</h2>
            <p>{message}</p>
            <p><b>💡 Try this:</b> {activity}</p>
            <h3>Vibe Level: {vibe}%</h3>
        </div>
        """,
        unsafe_allow_html=True
    )