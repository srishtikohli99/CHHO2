# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 04:40:29 2019

@author: srishti
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 07:56:12 2019

@author: srishti
"""

import requests
import json
import flask
from flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/123')
def hello():
    return render_template("upload.html")


@app.route('/uploader',methods = ['POST', 'GET'])
def result():
   

    if request.method == 'POST':
        file=request.files['file']
        name=file.filename
   
    filename=name
    api_key='949ce6a31c88957'
    language='pol'
    payload = {
               'isOverlayRequired': False,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    test_file= r.content.decode()
    text = json.loads(test_file)["ParsedResults"][0]["ParsedText"]
    return text

if __name__ == '__main__':
    app.run(debug=True)
#test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')