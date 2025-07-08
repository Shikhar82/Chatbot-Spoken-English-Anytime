# 🎙️ AI Spoken English Chatbot

Welcome to the **AI Spoken English Chatbot** — a smart, interactive chatbot that helps you practice your English speaking skills with real-time voice input and AI-powered grammar correction and feedback!

🌐 Live Demo: [chatbotshikhar.com](https://www.chatbotshikhar.com)

---

## ✨ Features

- 🎤 **Mic-based voice input** – Speak naturally using your device's mic
- ✅ **AI-powered transcription** – Converts your speech to text
- 🧠 **Grammar correction** – Fixes and improves your sentence
- 🤖 **AI reply with voice response** – Chatbot replies with voice and text
- 💡 **Speaking topic suggestions** – Get new topics to practice with

---

## 🧠 Built With

- [Streamlit](https://streamlit.io/)
- [AWS EC2](https://aws.amazon.com/ec2/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude](https://www.anthropic.com/index/claude)
- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pydub](https://pypi.org/project/pydub/)
- Nginx (for reverse proxy and HTTPS)
- Python 3.x

---

## 🚀 How It Works

1. **User speaks** through the mic
2. 🎧 Voice is captured and transcribed to text
3. ✍️ Text is grammatically corrected using Claude via Bedrock
4. 💬 Chatbot generates a meaningful reply
5. 🔊 Reply is converted to speech and played back to the user
6. 🎞️ A talking AI avatar is displayed during response playback

---

## 📁 Project Structure

chatbot/
│
├── chatbot_ui.py # Streamlit UI frontend
├── chatbot_logic.py # Backend logic: transcription, grammar fix, TTS, LLM
├── static/
│ └── ai_talking.gif # Talking avatar animation
├── robot.json # Lottie animation file
├── courselogo.png # Site logo
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run chatbot_ui.py

 Environment Variables / AWS Setup
Configure your AWS CLI:
aws configure

Ensure Bedrock access is granted in your region (us-east-1 recommended).

ChatBedrock from langchain-aws is used for Claude integration.

🙋‍♂️ Created By
Shikhar Verma
💬 Educator | DevOps Architect | Python Expert
🌐 www.chatbotshikhar.com
📧 shikhardevops@email.com
