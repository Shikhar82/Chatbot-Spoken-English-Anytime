# === chatbot_ui.py (Mic-Only Version) ===
import streamlit as st
import chatbot_logic as logic
from langchain.memory import ConversationSummaryBufferMemory
from streamlit_mic_recorder import mic_recorder
from streamlit_lottie import st_lottie
import requests
import json

# === Meta Tags for Social Sharing ===
st.markdown("""
    <meta property="og:title" content="AI Spoken English Chatbot | Shikhar Verma">
    <meta property="og:description" content="Practice spoken English with AI feedback and voice response.">
    <meta property="og:image" content="https://www.chatbotshikhar.com/courselogo.png">
    <meta property="og:url" content="https://www.chatbotshikhar.com">
    <meta name="twitter:card" content="summary_large_image">
""", unsafe_allow_html=True)

# === Page Config ===
st.set_page_config(
    page_title="Spoken English Chatbot",
    page_icon="https://www.chatbotshikhar.com/courselogo.png",
    layout="centered"
)

# === Load Robot Animation ===
def load_lottie_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

lottie_robot = load_lottie_file("robot.json")

# === Header with Robot Animation ===
with st.container():
    col1, col2 = st.columns([1.5, 6])
    with col1:
        st.markdown("<div style='margin-top: -50px; margin-bottom: -20px;'>", unsafe_allow_html=True)
        st_lottie(lottie_robot, height=150, key="robot")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <h1 style='margin-bottom: 4px; font-size: 2.1rem;'>🎙️ AI Spoken English Chatbot</h1>
            <p style='margin-top: 0px; font-size: 1.05rem;'>Improve your spoken English by talking to the bot and getting grammar corrections!</p>
        """, unsafe_allow_html=True)

# === Session Setup ===
if 'llm' not in st.session_state:
    st.session_state.llm = logic.get_llm_model()

if 'memory' not in st.session_state:
    st.session_state.memory = ConversationSummaryBufferMemory(llm=st.session_state.llm, max_token_limit=300)

# === SPEAKING SECTION ===
st.subheader("🎙️  Speak into the Mic to Practice")

audio_bytes = mic_recorder(start_prompt="Click to Speak", stop_prompt="Stop", just_once=True, key="mic")

if audio_bytes and 'bytes' in audio_bytes:
    st.audio(audio_bytes['bytes'], format='audio/wav')

    transcribed_text = logic.speech_bytes_to_text(audio_bytes['bytes'])

    if transcribed_text:
        st.success("📝 Transcribed Text:")
        st.markdown(transcribed_text)

        corrected_text = logic.correct_grammar(transcribed_text)
        st.info("✅ Corrected Sentence:")
        st.markdown(corrected_text)

 #       response = logic.generate_response(corrected_text, st.session_state.llm, st.session_state.memory)

        # ⏳ Show placeholder while voice is being generated
        placeholder_status = st.empty()
        placeholder_status.info("⏳ Please wait... AI is processing your voice response.")
        response = logic.generate_response(corrected_text, st.session_state.llm, st.session_state.memory)
        audio_path = logic.text_to_speech(response)

        if audio_path:
            placeholder_status.success("☺️ AI is responding via voice...")

            # 👇 Show AI talking GIF
            avatar_gif_url = "https://www.chatbotshikhar.com/assets/ai_talking.gif"
            html_code = f"""
            <div style="text-align:center; margin-bottom: 10px;">
                <img src="{avatar_gif_url}" width="150" alt="AI Talking">
            </div>
            """
            st.markdown(html_code, unsafe_allow_html=True)

            st.audio(audio_path, format="audio/mp3")

        # 💬 Show text response
        st.success("🤖 AI Reply:")
        st.markdown(response)

# === SUGGEST TOPIC BUTTON ===
if st.button("💡 Suggest a New Speaking Topic"):
    topic = logic.suggest_topic()
    st.info(f"🗣️  Try speaking on this: **{topic}**")

# === FOOTER ===
st.markdown("""
<hr style="margin-top:30px;">
<div style='text-align: center; color: gray'>
    Created by Shikhar Verma | 💬 AI Spoken English Chatbot | Powered by AWS Bedrock
</div>
""", unsafe_allow_html=True)
