from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS, cross_origin

from preprocessing import DecodeFileToBase64
import SpeechToText

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods = ['POST'])
@cross_origin()
def predictRoute():
    audioFile = request.json['sound']
    DecodeFileToBase64(audioFile, "AudioFile.wav")
    result = SpeechToText.SpeechToTextConversion("AudioFile.wav")
    return jsonify({"Result" : str(result)})




if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
