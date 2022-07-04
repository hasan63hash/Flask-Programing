from flask import Flask, render_template, request, url_for, Response
import requests
import os
from werkzeug.utils import secure_filename
from waitress import serve
from flask_qrcode import QRcode

UPLOAD_FOLDER = './static/images'
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024 # 32 MB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ip_str = "192.168.2.206"
port = 80

qm = QRcode(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/qr")
def qr():
    return render_template('qr.html')

@app.route("/get_qr", methods=["POST"])
def get_qr():
    my_qr = qm.qrcode("https://youtube.com")
    return Response(response=my_qr, status=200, mimetype="image/png")

@app.route("/upload", methods=["POST"])
def upload():
        if 'file' not in request.files:
            return "Ekte dosya yok"
        else:
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Resim yüklendi"

@app.route("/make_post_request")
def make_post_request():
    resp = requests.post("http://" + ip_str + ":" + str(port) + "/upload")
    return resp.content

if __name__ == "__main__":
    serve(app, host=ip_str, port=port)
