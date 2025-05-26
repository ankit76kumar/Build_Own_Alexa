
# 🗣️ Personal Voice Assistant with Python (Alexa Clone)

This is a simple Python-based voice assistant that listens to your voice commands and performs basic actions like playing songs on YouTube. It works similarly to Amazon Alexa, built using libraries like `speech_recognition`, `pyttsx3`, and `pywhatkit`.

---

## 🎯 Objective

The goal of this project is to:
- Create a **simple voice assistant** using Python.
- Learn about **speech-to-text**, **text-to-speech**, and **voice command processing**.
- Integrate the assistant with **YouTube search** for media playback.

---

## 🚀 Features

- 🎙️ Listens to voice commands using your system microphone.
- 🧠 Recognizes the keyword **"Alexa"** to activate listening.
- 🔊 Responds using speech (text-to-speech).
- 🎵 Plays songs from YouTube when you say:  
  > "Alexa, play [song name]"

---

## ⚙️ How It Works

- Uses `speech_recognition` to capture and convert speech to text.
- Uses `pyttsx3` for converting text responses to speech.
- Uses `pywhatkit` to play the requested song directly on YouTube.

---

## 🛠️ Requirements

Install required packages using pip:

```bash
pip install speechrecognition pyttsx3 pywhatkit pyaudio
````

> ⚠️ Note: For `pyaudio`, you might need to install a precompiled wheel on Windows. You can download it from [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## 📁 Files to Include in the Repository

```
voice-assistant-alexa-clone/
│
├── alexa_voice_assistant.py          # Main script
├── requirements.txt                  # Dependencies
├── README.md                         # Documentation (this file)
└── sample_output.png (optional)      # Screenshot or terminal output
```

---

## 📜 Sample Code Snippet

```python
if 'play' in command:
    song = command.replace('play', '')
    talk('Playing ' + song)
    pywhatkit.playonyt(song)
```

---

## 🔮 Future Enhancements

* Add commands for:

  * Telling time
  * Telling jokes
  * Fetching weather or news
* Add wake-word detection instead of continuous looping
* Create a GUI using **Tkinter** or **PyQt**
* Integrate with APIs (e.g., OpenAI, Google Search, etc.)

---

## 👨‍💻 Author

**Ankit Kumar**
🎓 B.Tech – Artificial Intelligence & Data Science
🏫 Truba Institute of Engineering & Information Technology
📍 Bhopal, Madhya Pradesh

---

## 🧾 License

This project is open-source under the [MIT License](LICENSE). Use it freely for learning and development.

---

⭐ Star this repository if you found it helpful, and feel free to fork it for your own experiments!

````

---

## 📄 `requirements.txt`

```txt
speechrecognition
pyttsx3
pywhatkit
pyaudio
````

