# 🌍 Voice Translator Web Application

A web-based voice translation app that recognizes spoken voice, translates it into a selected language, and reads the translated output aloud. Designed to eliminate language barriers in travel, communication, and social networking.

## 🎯 Features

- 🎤 **Voice Recognition** – Capture and convert speech to text in real time
- 🌐 **Language Translation** – Translate recognized text into a selected language
- 🔊 **Text-to-Speech** – Read aloud the translated text using speech synthesis
- 💻 **Web-based Interface** – Easy-to-use UI accessible through any modern browser

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **APIs & Libraries:**
  - `SpeechRecognition` – for capturing and converting voice to text
  - `Googletrans` – for language translation
  - `gTTS` or `pyttsx3` – for text-to-speech conversion
  - `Django` – for server-side logic and routing

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/ChilukuriSivaKarthikeya/Voice-translator-project.git

# Navigate into the project directory
cd Voice-translator-project

# Install dependencies (make sure virtualenv is activated)
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

