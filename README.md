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
<img width="1562" height="299" alt="Screenshot 2025-07-20 214714" src="https://github.com/user-attachments/assets/37fdac12-2d2c-450b-9164-5d30eb86e992" />
<img width="1920" height="1080" alt="Screenshot (1718)" src="https://github.com/user-attachments/assets/e278cd67-2ab6-4ed2-9e07-f37f26ea82cf" />
<img width="1920" height="1080" alt="Screenshot (1719)" src="https://github.com/user-attachments/assets/80a1bdf9-6f99-414c-98e0-7d8d6508d49a" />

---

## 📎 References

- [📄 Presentation Link](https://docs.google.com/presentation/d/1MFLKM0DI1R1VPdDdIxZIijRnnMWFqdtw/edit?usp=drive_link\&ouid=113207388992091567067\&rtpof=true\&sd=true)

---
