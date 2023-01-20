from unittest import result
import cv2
import os
from PIL import Image
from numpy import asarray
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model

model = load_model('digit_recognizer.h5')

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = 'static/'

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True) 