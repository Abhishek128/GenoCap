from flask import Flask , render_template , request
from flask.globals import request 
import os
import requests
import mimetypes
import json

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
@app.route("/",methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST' :
        file = request.files['image'] 
        filename = file.filename
        filepath = UPLOAD_FOLDER+'/'+filename[:-4]+'.png'
        file.save(filepath)
        url_en = 'http://max-image-caption-generator.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict'
        img_path = './static/img/test/1.jpg'
        img_path = filepath
        mime_type = mimetypes.guess_type(img_path)[0]
        with open(img_path, 'rb') as img_file:
            file_form = {'image': (img_path, img_file, mime_type)}
            r = requests.post(url=url_en, files=file_form)
            data = r.json()
            caption = []
            for obj in data['predictions'] :
                caption.append(obj['caption'])
        return render_template('index.html',caption = caption,path = img_path)
    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug=True)