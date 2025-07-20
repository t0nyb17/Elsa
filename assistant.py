import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
from AppOpener import open as open_app
import pyautogui
import re

class Assistant:
    def __init__(self, log_queue):
        self.log_queue = log_queue
        self.is_listening = False
        self.recognizer = sr.Recognizer()
        self.speech_engine = pyttsx3.init()
        voices = self.speech_engine.getProperty('voices')
        self.speech_engine.setProperty('voice', voices[1].id)

    def log(self, message):
        self.log_queue.put(message)

    def talk(self, text):
        self.log(f'Elsa: {text}')
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listen_for_command(self):
        command = ""
        try:
            with sr.Microphone() as source:
                self.log("Elsa is listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio)
                self.log(f'User said: {command}')
        except sr.UnknownValueError:
            self.talk("Sorry, I didn't catch that. Could you please repeat?")
        except Exception as e:
            self.log(f"Error during speech recognition: {e}")
            self.talk("I'm having trouble listening right now.")
        return command.lower()

    def stop(self):
        self.is_listening = False

    def run(self):
        self.is_listening = True
        self.talk("Elsa online. How can I assist you?")
        while self.is_listening:
            command = self.listen_for_command()
            if not command:
                continue
            if 'stop' in command or 'exit' in command or 'shutdown' in command:
                self.talk('Shutting down. Goodbye!')
                self.stop()
            elif 'time' in command:
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                self.talk('The current time is ' + current_time)
            elif 'search for' in command:
                search_query = command.replace('search for', '').strip()
                self.talk(f'Searching Google for {search_query}')
                webbrowser.open(f'https://www.google.com/search?q={search_query}')
            elif 'wikipedia' in command:
                search_query = command.replace('wikipedia', '').strip()
                try:
                    self.talk(f'Searching Wikipedia for {search_query}')
                    result = wikipedia.summary(search_query, sentences=2)
                    self.talk(result)
                except Exception:
                    self.talk(f'Sorry, I could not find a Wikipedia page for {search_query}.')
            elif 'open youtube' in command:
                self.talk('Opening YouTube')
                webbrowser.open('https://youtube.com')
            elif 'open' in command:
                app_name = command.replace('open', '').strip()
                self.talk(f"Trying to open {app_name}")
                try:
                    open_app(app_name, match_closest=True)
                except Exception:
                    self.talk(f"Sorry, I couldn't find or open {app_name}.")
            elif 'take a screenshot' in command:
                try:
                    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    pyautogui.screenshot(filename)
                    self.talk(f"Screenshot saved as {filename}")
                except Exception:
                    self.talk("I was unable to take a screenshot.")
            elif 'calculate' in command:
                match = re.search(r'(\d+)\s*(plus|\-|\*|/)\s*(\d+)', command)
                if match:
                    num1 = int(match.group(1))
                    operator = match.group(2)
                    num2 = int(match.group(3))
                    if operator == 'plus':
                        result = num1 + num2
                    self.talk(f"The result is {result}")
                else:
                    self.talk("I couldn't understand the calculation. Please say something like 'calculate 5 plus 5'.")
            else:
                pass
