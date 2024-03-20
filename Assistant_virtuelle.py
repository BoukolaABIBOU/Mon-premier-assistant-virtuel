# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:02:04 2022

@author: ABIBOU Boukola
"""

import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', 'french')

def parler (text):
    engine.say(text)
    engine.runAndWait()
    
     
def ecouter():
    try:
        with sr.Microphone() as source:
           print("parlez maintenant")
           voix=listener.listen(source)
           command=listener.recognize_google(voix ,language='en')
           command.lower()

    except:
        pass
    return command

def lancer_assistant():
    command = ecouter()
    print(command)
    if 'mets la chanson de' in (command):
        chanteur=command.replace('mets la chanson de')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif'heure' in (command):
        heure=datetime.datetime.now('%H:%M')
        parler('il est'+heure)
    elif 'bonjour' in command:
        print('Bonjour,ça va ?')
    else:
        print('Je ne comprends pas')
        
while True:    
   lancer_assistant()
