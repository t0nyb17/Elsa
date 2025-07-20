# 🧊 Elsa – Personal Voice-Controlled Automation Assistant (Web Interface)

Elsa is a browser-based personal assistant built with Python Flask for the backend and HTML/CSS for the frontend. It listens to your voice commands and performs basic desktop tasks like opening apps, taking screenshots, fetching quick info from Google/Wikipedia, and more.

---

## 🚀 Features

- 🎤 **Voice Interaction**: Interact with your system using simple voice commands.
- 🖥️ **Web Interface**: Smooth, minimalistic browser interface with live status and logs.
- 🟢 **Start/Stop Controls**: Easily manage Elsa's activity from the browser.
- 📝 **Real-time Activity Logs**: See live logs of commands and responses.
- ⚡ **Automation Commands**:
  - Current time queries
  - Google search
  - Wikipedia summaries
  - Open YouTube
  - Launch desktop apps
  - Take system screenshots
  - Basic arithmetic calculations

---

## 📁 Project Structure

```
project/
│
├── app.py               # Flask backend server
├── assistant.py         # Voice assistant automation logic
├── templates/
│   └── index.html       # Frontend UI page
└── static/
    └── css/
        └── style.css    # CSS styling for frontend
```

---

## 🛠️ Setup Guide

### 1. Install Python Packages

```bash
pip install flask speechrecognition pyttsx3 wikipedia AppOpener pyautogui
```

**Microphone Support:**

- For `pyaudio` (speech input):
  - Windows:
  ```bash
  pip install pipwin && pipwin install pyaudio
  ```
  - Linux:
  ```bash
  sudo apt-get install portaudio19-dev && pip install pyaudio
  ```

### 2. Start Flask Server

```bash
python app.py
```

Open your browser at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🖥️ How to Use Elsa

- Launch the application in your browser.
- Click **Initialize** to activate the voice assistant.
- Supported commands include:
  - "What time is it?"
  - "Search for latest tech news"
  - "Wikipedia Python programming"
  - "Open YouTube"
  - "Take a screenshot"
  - "Calculate 10 plus 15"
  - "Stop" or "Shutdown" to deactivate Elsa.

---

## 📸 Screenshots / Demo

---

## 📎 References

- [📄 Presentation Link](https://docs.google.com/presentation/d/1MFLKM0DI1R1VPdDdIxZIijRnnMWFqdtw/edit?usp=drive_link\&ouid=113207388992091567067\&rtpof=true\&sd=true)

---

## 📃 License

MIT License — Free to use, modify, and distribute.

---

Happy Automating with Elsa! 🎉

