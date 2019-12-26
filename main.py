import speech_recognition as sr
import webbrowser as wb
from time import ctime , sleep , strftime
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False) :
    with sr.Microphone() as source :
        print("Say something")
        if ask:
            alix_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try :
            voice_data = r.recognize_google(audio,key=None,language='en-US')
            print(voice_data)
        except sr.UnknownValueError :
            alix_speak("Sorry i didn't get what you said")
        except sr.RequestError:
            alix_speak("Sorry , speech service is down")
        return voice_data
    
def alix_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1,10000000)
    audio_file = f"audio-{str(r)}.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
 
    os.remove(audio_file)

def respond (voice_data):
    print("you have said : " + voice_data)
    if 'what is your name' in voice_data:
        alix_speak("My name is Alix")
    if 'what time is it' in voice_data:
        alix_speak(strftime("%H %M "))
    if 'search' in voice_data:
        search = record_audio("What do you want me to search ?")
        url = f"https://www.google.com/search?q={search}"
        wb.get().open(url)
        alix_speak(f"Here the result for {search}")
    if 'find location' in voice_data:
        location = record_audio("What is the location ?")
        url = f"https://www.google.nl/maps/place/{location}/&amp"
        wb.get().open(url)
        alix_speak(f"Here is what i found on google map for {location} ")
    if "exit" in voice_data :
        exit()
 

        

alix_speak("How can i help you ?")
while True :
    voice_data = record_audio() 
    sleep(1)
    respond(voice_data)
