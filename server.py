from flask import Flask, request
from EmotionDetection import emotion_detection
app = Flask(__name__)
@app.route('/emotionDetector')
def home():
    textToAnalyze = request.args.get('textToAnalyze')
    emotion = emotion_detection.emotion_detector(textToAnalyze)
    return "For the given statement, the system response is 'anger': "+emotion["anger"]+", 'disgust': "+emotion["disgust"]+", 'fear': "+emotion["fear"]+", 'joy': "+emotion["joy"]+" and 'sadness': "+emotion["sadness"]+". The dominant emotion is "+emotion["dominant_emotion"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)