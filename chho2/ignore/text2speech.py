# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:17:49 2019

@author: srishti
"""

import voicerss_tts

voice = voicerss_tts.speech({
    'key': 'a2ac06c58a544190af338e8e286d7f4e',
    'hl': 'en-us',
    'src': 'I love you,Rahul!',
    'r': '0',
    'c': 'wav',
    'f': '44khz_16bit_stereo',
    'ssml': 'false',
    'b64': 'false'
})

newFile = open ("speech.wav", "wb")
newFile.write(voice['response'])
newFile.close()
