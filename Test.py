from flask import Flask, request, make_response
from datetime import datetime
import os

app = Flask(__name__)
IMG_PATH = "E:/data/"


@app.route('/display/img/<string:filename>', methods=['GET'])
def display_img(filename):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(IMG_PATH + filename, "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response
    else:
        pass
