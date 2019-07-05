# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:24:08 2019

@author: srishti
"""

import requests
import uuid
import json
import flask
import voicerss_tts
import os
from werkzeug import secure_filename
import speech_recognition as sr 
import sqlite3
from flask import Flask, render_template, request,redirect,send_from_directory,send_file
app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def ocr_space_file(filename, overlay=False, api_key='949ce6a31c88957', language='eng'):
    

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


@app.route('/')
def hello():
    return render_template('index.html')
    #return "hello"

@app.route('/uploader',methods = ['POST', 'GET'])
def result():
   
    if request.method == 'POST':
        text=request.form['text']
        sentences=request.form['number']
        url = "https://api.meaningcloud.com/summarization-1.0"
        payload = "key=56dee7c0872448b1b09b2f4d8d339d66&txt="+text+"&sentences="+sentences
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, data=payload, headers=headers)
        summary=json.loads(response.text)["summary"]
        return summary
    return "fail"

@app.route('/ttos',methods = ['POST', 'GET'])
def ttos():
    if request.method == 'POST':
        voice = voicerss_tts.speech({
        'key': 'a2ac06c58a544190af338e8e286d7f4e',
        'hl': 'en-us',
        'src': request.form['ttos'],
        'r': '0',
        'c': 'wav',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'false'
        })
        target = os.path.join(APP_ROOT, 'speech/')
        id = uuid.uuid1()
        filename=str(id)+".wav"
        
        if not os.path.isdir(target):
            os.mkdir(target)
        destination = "/".join([target, filename])
        newFile=open(destination,"wb")
        newFile.write(voice['response'])
        newFile.close()
        return send_file(destination,as_attachment=True) 
        return redirect('/')
        #return redirect('/')
        
        
@app.route('/ocr',methods = ['POST', 'GET'])
def ocr():
    target = os.path.join(APP_ROOT, 'images/')
    #print("yeh target hai")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        test_file = ocr_space_file(filename=destination, language='eng')
        va=json.loads(test_file)
        msg=va["ParsedResults"][0]["ParsedText"]
        print(msg)
    return msg
  
@app.route('/stot',methods = ['POST', 'GET'])
def stot():
    target = os.path.join(APP_ROOT, 'audio/')
    #print("yeh target hai")
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist("audio"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    AUDIO_FILE = (destination) 
    # use the audio file as the audio source 
      
    r = sr.Recognizer() 
    
    with sr.AudioFile(AUDIO_FILE) as source: 
        #reads the audio file. Here we use record instead of 
        #listen 
        audio = r.record(source)   
      
    try: 
        return "The audio file contains: " + r.recognize_google(audio) 
      
    except sr.UnknownValueError: 
        return "Google Speech Recognition could not understand audio" 
      
    except sr.RequestError as e: 
        return "Could not request results from Google Speech Recognition service; {0}".format(e)
    
    
if __name__ == '__main__':
    app.run(debug=True)