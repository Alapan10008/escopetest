import re
from turtle import pos
from flask import send_file
from flask import Flask,request,jsonify
from flask_restful import Api,Resource
import os 
import soundfile
import numpy as np
import librosa as lib
import requests
from lowpass_filter import butter_lowpass_filter
from fft import plot_magnitude_spectrum_new
import werkzeug



app=Flask(__name__)
api=Api(app)


@app.route("/fft", methods=["POST"])
def fft():
 if request.method == "POST" :
            audio_file = request.files["file"]
            if not audio_file:
                return "No audio uploaded",400
            filename = werkzeug.utils.secure_filename(audio_file.filename)
         
            print(filename)
            audio_file.save(filename)
            wav_loc = str(filename)
            audio,sr=lib.load(wav_loc)
            os.remove(filename) 
            
            filename = filename.split(".")[0]
            cutoff = 300
            order = 2  
            nq=(0.5*sr)
            y = butter_lowpass_filter(audio, cutoff, sr, order,nq)    
            img =plot_magnitude_spectrum_new(y, sr, filename, 0.03)
            return send_file(img, mimetype='image/png')
    

    
@app.route("/noisereduser", methods=["POST"])
def noisereduser():
    if request.method == "POST" :
            audio_file = request.files["file"]
            # if not audio_file:
            #     return "No audio uploaded",400
            filename = werkzeug.utils.secure_filename(audio_file.filename)
            audio_file.save(filename)
            wav_loc = str(filename)
            audio,sr=lib.load(wav_loc)
            os.remove(filename) 
            filename = filename.split(".")[0]
            cutoff = 300
            order = 2  
            nq=(0.5*sr)
            y = butter_lowpass_filter(audio, cutoff, sr, order,nq)
            soundfile.write(filename+'.wav', y, sr)
    
            return send_file(
            filename+'.wav',
            mimetype="audio/wav", 
            as_attachment=True, 
            attachment_filename=filename+'.wav')


@app.route("/helloworld", methods=["POST"])
def Helloworld():
    
    return "Hello world"
        
if __name__=="__main__"  :
    app.run(debug=True,)  
    
    
