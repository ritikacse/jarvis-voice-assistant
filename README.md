# jarvis-voice-assistant
A Python-based Jarvis voice assistant that uses speech recognition, text-to-speech, computer automation, and DeepSeek AI to perform tasks and answer user queries.
# Jarvis Voice Assistant

A Python-based voice assistant that can understand voice commands, perform basic computer tasks, and use DeepSeek AI to answer general questions.

## Features

* Voice input using Speech Recognition
* Text-to-speech responses
* Tell the current time
* Open YouTube
* Open Google
* Google search
* Open Windows Notepad
* Take screenshots
* AI responses using DeepSeek
* Voice-controlled exit command

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* PyAutoGUI
* OpenAI Python SDK
* DeepSeek API

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
DEEPSEEK_API_KEY=YOUR_API_KEY
```

Run the assistant:

```bash
python jarvis.py
```

## Example Commands

You can say:

* "What is the time?"
* "Open YouTube"
* "Open Google"
* "Search Python tutorials"
* "Open Notepad"
* "Take a screenshot"
* "Stop"

## Security

The API key should never be written directly inside `jarvis.py` or committed to GitHub.

Use an environment variable stored in `.env`.

## Author

Ritika Chauhan
