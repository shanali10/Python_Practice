import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import googlesearch
import os
import random
import wikipedia

# Windows default voices are only 2.
# 0 is male and 1 is female.


windowsEngine = pyttsx3.init('sapi5')
windowsVoices = windowsEngine.getProperty('voices')
windowsEngine.setProperty('voice', windowsVoices[1].id)


def speak(alphaAudio):
    windowsEngine.say(alphaAudio)
    windowsEngine.runAndWait()


def routine():
    print("Hello Sir! I am Alpha, and How can I help You!")
    speak("Hello Sir! I am Alpha, and How can I help You!")


def userCommand():
    # User Microphone Commands...
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)

        print("Voice Recognizing...")


    except Exception:
        print("Sorry! Voice did not recognized, Can You Repeat again?")
        speak("Sorry! Voice did not recognized, Can You Repeat again?")
        return "Error"

    return command


if __name__ == '__main__':
    routine()
    while True:
        command = userCommand().lower()
        if 'wikipedia' in command:
            try:
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences=2)
                speak("wikipedia says:")
                print(results)
                speak(results)

            except Exception:
                print("wikipedia searching failed...")
                speak("wikipedia searching failed...")


        elif 'google search' in command:
            try:
                data = googlesearch
                print(data)
                speak(data)
            except Exception:
                print("wikipedia searching failed...")
                speak("wikipedia searching failed...")

        elif 'open youtube' in command:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open facebook' in command:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in command:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open programs' in command:
            os.open("F:\\")

        elif 'open d' in command:
            os.open("D:\\")

        elif 'open installed programs' in command:
            os.open("E:\\")

        elif 'play sufi' in command:
            directory = "D:\\shan\\Qawali"
            qawalis = os.listdir(directory)
            ran = random.randint(0, len(qawalis) - 1)
            os.startfile(os.path.join(directory, qawalis[ran]))

        elif 'who is shan' or 'who is shan ali mughal' or 'who is shan ali' in command:
            print("Shan Ali Mughal is creator and owner of Alpha. "
                  "He is from Muzaffarabad Azad Kashmir. "
                  "He is learning programming from the internet and "
                  "he loves to do code. he loves his work")

            # speak("Shan Ali Mughal is creator and owner of Alpha. "
            #       "He is from Muzaffarabad Azad Kashmir. "
            #       "He is learning programming from the internet and"
            #       "he loves to do code. he loves his work")


        elif 'time' in command:
            tim = datetime.datetime.now().strftime("%H:%M:%S")
            speak(tim)

        # elif 'creator' or 'owner' or 'god' or 'who made you' in command:
        #     print("Shan Ali Mughal is my creator and owner.")
        #     speak("Shan Ali Mughal is my creator and owner.")

        elif 'exit' in command:
            print('Thank You for your time. See you later...')
            speak('Thank You for your time. See you later...')
            exit()
