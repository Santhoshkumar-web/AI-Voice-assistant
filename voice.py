import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def list_available_voices():
    eng = pyttsx3.init()
    voices = eng.getProperty('voices')
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.id}")

def voiceChange():
    # Uncomment and adjust the voice ID to select your preferred cute female voice
    # list_available_voices()
    cute_female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', cute_female_voice_id)
    engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is {}/{}/{}".format(date, month, year))

def wishme():
    speak("Welcome back darling!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning darling")
    elif 12 <= hour < 18:
        speak("Good afternoon darling")
    elif 18 <= hour < 24:
        speak("Good Evening darling")
    else:
        speak("Good night darling")
    speak("Hi Darling, this is Samantha, your AI assistant. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again, please...")
            return "none"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com', '123')
    server.sendmail('test@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    voiceChange()
    wishme()

    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What Should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent successfully!")

            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome'in query:
            speak("What should i Search ?")
            chromepath  = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir ='D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir , songs[1]))



        elif 'offline' in query:
            speak("Goodbye darling, see you soon!")
            quit()
