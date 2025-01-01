import os
import time
import webbrowser
import speech_recognition as sr
import datetime
import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer
import pyttsx3

assistant_name = "Echo Echo"

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return listen()
    except sr.RequestError:
        speak("Speech recognition service is not available.")
        return "None"

def chat_with_ai(input_text):
    new_user_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    chat_history_ids = new_user_input_ids
    bot_output = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, no_repeat_ngram_size=3, top_k=50, top_p=0.95, temperature=0.7)
    bot_response = tokenizer.decode(bot_output[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak(f"I am {assistant_name}. How can I assist you today?")

def process_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "play music" in command:
        speak("Opening YouTube Music")
        webbrowser.open("https://music.youtube.com")

    elif "open spotify" in command:
        speak("Opening Spotify")
        subprocess.Popen(["C:\\Users\\YourUsername\\AppData\\Spotify\\Spotify.exe"]) 

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])

    elif "open camera" in command:
        speak("Opening camera")
        os.system("start microsoft.windows.camera:")

    elif "time" in command:
        current_time = time.strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "reminder" in command:
        speak("What should I remind you about?")
        reminder = listen()
        speak(f"Setting a reminder for {reminder}")
        with open("reminders.txt", "a") as file:
            file.write(f"Reminder: {reminder} - {datetime.datetime.now()}\n")

    elif "to do list" in command:
        speak("Do you want to add or read the to-do list?")
        action = listen()
        if "add" in action:
            speak("What should I add to your to-do list?")
            task = listen()
            with open("todo.txt", "a") as file:
                file.write(f"{task}\n")
            speak(f"Added {task} to your to-do list.")
        elif "read" in action:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.readlines()
                    if tasks:
                        speak("Your to-do list contains the following items:")
                        for task in tasks:
                            speak(task.strip())
                    else:
                        speak("Your to-do list is empty.")
            except FileNotFoundError:
                speak("No to-do list found.")

    elif "set alarm" in command:
        speak("Please tell me the time to set the alarm in HH:MM format.")
        alarm_time = listen()
        speak(f"Setting an alarm for {alarm_time}")
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                speak("Alarm ringing. Wake up!")
                break
            time.sleep(10)

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Let's chat!")
        while True:
            user_input = listen()
            if 'exit' in user_input or 'quit' in user_input:
                speak("Goodbye!")
                break
            ai_response = chat_with_ai(user_input)
            print(ai_response)
            speak(ai_response)
def main():
    greet_user()
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
