# **ECHO ECHO - Voice Assistant with AI Chatbot**

ECHO ECHO is a Python-based voice assistant that integrates speech recognition, natural language processing (NLP), and AI-driven chatbot functionality to provide a seamless voice-driven user experience. It allows users to interact with their computers through voice commands and responses powered by AI. ECHO ECHO can open applications like Spotify, Notepad, and more, as well as handle tasks such as reminders, to-do lists, alarms, and web searches. With built-in text-to-speech (TTS) capabilities, ECHO ECHO delivers a human-like voice to communicate with users.

---

## **Features**

- **Voice Commands**: Use voice commands to interact with your computer (e.g., opening apps, checking the time, setting reminders).
- **AI Chatbot**: Converse with ECHO ECHO using the DialoGPT model, which generates conversational responses.
- **Text-to-Speech**: ECHO ECHO speaks back to you with human-like voice output, using the `gTTS` library.
- **Speech Recognition**: Listen to user input using the `speech_recognition` library, converting speech to text.
- **App Control**: Open and control popular apps like Spotify, YouTube, Notepad, and more.
- **Reminders and To-Do Lists**: Set and manage reminders, and add/remove tasks in your to-do list.
- **Time & Date Info**: Get the current time and date with voice output.
- **Alarm Functionality**: Set and manage alarms for specific times.

---

## **Technologies Used**

- **Python** (v3.x)
- **Speech Recognition** (`speech_recognition` library)
- **Text-to-Speech** (`gTTS`, `pyttsx3`)
- **Transformers** (`Hugging Face`'s DialoGPT model for conversation)
- **Webbrowser** (for opening websites)
- **Subprocess** (for app control)
- **Time & Date Management** (`datetime`, `time`)

---

## **Installation**

1. Clone the repository:

   `git clone https://github.com/yourusername/echo-echo.git`

   `cd echo-echo`

2. Create a virtual environment (optional but recommended):

   `python -m venv venv`

   On Windows: `venv\Scripts\activate`

3. Install the required dependencies:

   `pip install -r requirements.txt`

   **Dependencies**:
   - `speech_recognition`
   - `gTTS`
   - `pyttsx3`
   - `transformers`
   - `webbrowser`
   - `subprocess`

---

## **Setup & Configuration**

### **Setting up Hugging Face's DialoGPT Model**
Make sure you have an internet connection to download the DialoGPT model from Hugging Face. The model is automatically loaded when you run the script, so there’s no need for manual downloading.

---

## **How to Use**

1. **Run the Script**: After installation, run the `main.py` script to start ECHO ECHO:

   `python main.py`

2. **Voice Commands**: ECHO ECHO will listen for commands and provide spoken responses. You can interact with it in the following ways:

   - **Open apps**: Say "Open Spotify", "Open YouTube", "Open Notepad", etc.
   - **Get information**: Ask "What is the time?", "What is the date?", etc.
   - **Create reminders**: Say "Set a reminder" and specify the task.
   - **Chat with AI**: Just start a conversation, for example, "Hi ECHO ECHO".
   
3. **Use the AI Chatbot**: You can also have a conversation with ECHO ECHO. Ask it questions, and it will respond using the DialoGPT model.

---

## **Commands You Can Use**

- **Open apps**: "Open YouTube", "Open Spotify", "Open Notepad", etc.
- **Get Time**: "What is the time?"
- **Get Date**: "What is the date?"
- **Set Reminder**: "Set a reminder for meeting at 3 PM"
- **Manage To-Do List**: "Add task to to-do list", "Read my to-do list"
- **Set Alarm**: "Set alarm for 7 AM"
- **Chat with AI**: "Hi ECHO ECHO", "How are you?", etc.

---

## **Troubleshooting**

- **Error in speech recognition**: Make sure your microphone is correctly configured and connected.
- **Model Loading Issues**: Ensure you have an internet connection, as the DialoGPT model is downloaded from Hugging Face.
- **Audio issues**: If the TTS output isn't working, make sure you have `gTTS` or `pyttsx3` properly installed.

---

