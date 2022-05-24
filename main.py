import speech_recognition as sr
import pyttsx3
import random
import pyaudio
import wave

r = sr.Recognizer()
words = ["привет", "как", "твои", "дела", "да"]
s = ""
n = 3


def SpeakText(command):
    enigne = pyttsx3.init()
    enigne.say(command)
    enigne.runAndWait()


for i in range(n):
    s += str(random.choice(words))
    s += " "
s = s[:-1]
print(s)

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)
    audio2 = r.listen(source2)

    Txt = r.recognize_google(audio2, language="ru-RU")
    Txt = Txt.lower()

    print(Txt)
    SpeakText(Txt)

if Txt == s:
    print("True")