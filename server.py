"""Expose emotion server"""
from flask import Flask, request
from EmotionDetection import emotion_detection
app = Flask(__name__)
@app.route('/emotionDetector')
def detector():
    """To get emotion"""
    text = request.args.get('textToAnalyze')
    emotion = emotion_detection.emotion_detector(text)
    if emotion["dominant_emotion"] == "None":
        return "Invalid text! Please try again!"
    return "For the given statement, the system response is 'anger': "+str(emotion["anger"])+", 'disgust': "+str(emotion["disgust"])+", 'fear': "+str(emotion["fear"])+", 'joy': "+str(emotion["joy"])+" and 'sadness': "+str(emotion["sadness"])+". The dominant emotion is "+str(emotion["dominant_emotion"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
