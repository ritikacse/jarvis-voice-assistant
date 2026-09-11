import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyautogui
from openai import OpenAI
from dotenv import load_dotenv

# ==========================================
# CONFIGURATION
# ==========================================

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.")
    exit()

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)


# ==========================================
# TEXT TO SPEECH
# ==========================================

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    """Convert text to speech."""

    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()


# ==========================================
# SPEECH RECOGNITION
# ==========================================

def listen():
    """Listen to the user's voice and convert it to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(audio)

        print("You:", query)

        return query.lower()

    except sr.UnknownValueError:

        print("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:

        print("Speech recognition service is unavailable.")
        return ""


# ==========================================
# DEEPSEEK AI
# ==========================================

def ask_ai(prompt):
    """Send the user's question to DeepSeek AI."""

    try:

        response = client.chat.completions.create(

            model="deepseek-chat",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful voice assistant. "
                        "Give clear and concise answers."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        print("AI Error:", e)

        return "Sorry, I am unable to connect to the AI service."


# ==========================================
# COMMAND FUNCTIONS
# ==========================================

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current_time}")


def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak(f"Today is {current_date}")


def open_youtube():

    webbrowser.open("https://www.youtube.com")

    speak("Opening YouTube.")


def open_google():

    webbrowser.open("https://www.google.com")

    speak("Opening Google.")


def google_search(query):

    search_query = query.replace("search", "", 1).strip()

    if not search_query:

        speak("What would you like me to search for?")

        return

    url = (
        "https://www.google.com/search?q="
        + search_query.replace(" ", "+")
    )

    webbrowser.open(url)

    speak(f"Searching Google for {search_query}")


def open_notepad():

    try:

        os.system("notepad.exe")

        speak("Opening Notepad.")

    except Exception:

        speak("I could not open Notepad.")


def take_screenshot():

    try:

        screenshot = pyautogui.screenshot()

        filename = "screenshot.png"

        screenshot.save(filename)

        speak("Screenshot has been taken.")

        print(f"Screenshot saved as {filename}")

    except Exception as e:

        print("Screenshot error:", e)

        speak("I could not take the screenshot.")


# ==========================================
# COMMAND EXECUTION
# ==========================================

def run_command(query):

    if not query:
        return True

    # -----------------------------
    # TIME
    # -----------------------------

    if "time" in query:

        tell_time()


    # -----------------------------
    # DATE
    # -----------------------------

    elif "date" in query or "today" in query:

        tell_date()


    # -----------------------------
    # YOUTUBE
    # -----------------------------

    elif "open youtube" in query:

        open_youtube()


    # -----------------------------
    # GOOGLE
    # -----------------------------

    elif "open google" in query:

        open_google()


    # -----------------------------
    # GOOGLE SEARCH
    # -----------------------------

    elif query.startswith("search"):

        google_search(query)


    # -----------------------------
    # NOTEPAD
    # -----------------------------

    elif "open notepad" in query:

        open_notepad()


    # -----------------------------
    # SCREENSHOT
    # -----------------------------

    elif "screenshot" in query:

        take_screenshot()


    # -----------------------------
    # EXIT
    # -----------------------------

    elif (
        "exit" in query
        or "quit" in query
        or "stop" in query
        or "goodbye" in query
    ):

        speak("Goodbye! Have a nice day.")

        return False


    # -----------------------------
    # AI FALLBACK
    # -----------------------------

    else:

        response = ask_ai(query)

        speak(response)

    return True


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    speak(
        "Hello! I am Jarvis, your voice assistant. "
        "How can I help you?"
    )

    while True:

        query = listen()

        if query:

            should_continue = run_command(query)

            if not should_continue:

                break


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main()
