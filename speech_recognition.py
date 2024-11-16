import os
import time
#import playsound
import SpeechRecognition as sr
from gtts import gTTS


def get_audio():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source,phrase_time_limit=5)
        said = r.recognize_google(audio)
        print(said)
        return said

    
n=5
ai={}
file=open("E:/py files/questions.py","a")
while n==5:
    print("Question")
    key=get_audio()
    key=key.lower()
    if key=="bye":
        break
    print("Say answer")
    value=get_audio()
    ai[key]=value
print(ai)
txt=str(ai)
print(txt)
file.write(txt)
file.close()
