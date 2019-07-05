# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:46:56 2019

@author: srishti
"""

import speech_recognition as sr
r= sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)
    print("Time up!")

try:
    text=r.recognize_google(audio)
    print(text)
except:
    print("Come again")