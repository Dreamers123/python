
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
import ssl
from time import ctime
import time
import webbrowser
import os # to remove created audio files
r = sr.Recognizer()

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
#webbrowser.get('chrome').open_new_tab(urL)
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        return voice_data

def respond(voice_date):
    if 'what is your name' in voice_data:
        print(voice_date)
        speak("My name is Jannat")
    if 'what time is it' in voice_data:
        print(voice_date)
        speak(ctime())
    if 'search'  in voice_data:
        search=record_audio("What you want to search?")
        url_1 = "https://google.com/search?q=" + search
        url_2 = "https://www.youtube.com/results?search_query="+ search
        webbrowser.get('chrome').open_new_tab(url_2)
        print("I have fount "+url_2)
    if 'find location'  in voice_data:
        search=record_audio("What is your location?")
        url_1 = "https://google.nl/maps/place/" + search
        webbrowser.get('chrome').open_new_tab(url_1)
        print("I have fount "+url_1)
    if 'exit' in voice_data:
        exit()



time.sleep(5)
while(5):
    speak("How can I help You ?")
    voice_data = record_audio()
    respond(voice_data)