import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=inputjson, headers=header)
    
    if response.status_code == 400:
        return {
            "anger": emotions["anger"], 
            "disgust": emotions["disgust"], 
            "fear": emotions["fear"], 
            "joy": emotions["joy"], 
            "sadness": emotions["sadness"]
        }
    else:
    responseJson = json.loads(response.text)
    emotions = responseJson["emotionPredictions"][0]["emotion"]
    response_dominant_emotion = {
        "anger": emotions["anger"], 
        "disgust": emotions["disgust"], 
        "fear": emotions["fear"], 
        "joy": emotions["joy"], 
        "sadness": emotions["sadness"]
    }
    highest_score_key = max(emotions, key=emotions.get)
    response_dominant_emotion["dominant_emotion"] = highest_score_key
    return response_dominant_emotion

  