from EmotionDetection import emotion_detection

def test1():
    assert emotion_detection.emotion_detector("I am glad this happened")["dominant_emotion"]=="joy"

def test2():
    assert emotion_detection.emotion_detector("I am really mad about this")["dominant_emotion"]=="anger"

def test3():
    assert emotion_detection.emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]=="disgust"

def test4():
    assert emotion_detection.emotion_detector("I am so sad about this")["dominant_emotion"]=="sadness"

def test5():
    assert emotion_detection.emotion_detector("I am really afraid that this will happen")["dominant_emotion"]=="fear"