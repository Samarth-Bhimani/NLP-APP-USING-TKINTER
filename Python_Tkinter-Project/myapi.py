import requests
import json

class API:

    def Sentiment(self,text):

        url = "https://api.edenai.run/v2/text/sentiment_analysis"

        payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "providers": "openai",
            "language": "en",
            "text": text
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFiMzFlOTktZWFmZS00YzZhLWJhZDAtMjQ3Y2ZkYjdiZGE0IiwidHlwZSI6ImFwaV90b2tlbiJ9.A2RKJHhsCWAj2p3jlfXarJPgPB3ZpAqoaPFqm5-jNTg"
        }

        response = requests.post(url, json=payload, headers=headers)

        ans = response.json()

        sentiment = ans['openai']['general_sentiment']
        sentiment_score = ans['openai']['general_sentiment_rate']

        return "{} --> {}".format(sentiment,sentiment_score)

    def NER(self,text):

        url = "https://api.edenai.run/v2/text/named_entity_recognition"

        payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "providers": "openai",
            "language": "en",
            "text": text
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFiMzFlOTktZWFmZS00YzZhLWJhZDAtMjQ3Y2ZkYjdiZGE0IiwidHlwZSI6ImFwaV90b2tlbiJ9.A2RKJHhsCWAj2p3jlfXarJPgPB3ZpAqoaPFqm5-jNTg"
        }

        response = requests.post(url, json=payload, headers=headers)

        ans = response.json()

        ner = ans['openai']['items'][0]['entity']
        ner_category = ans['openai']['items'][0]['category']
        ner_score = ans['openai']['items'][0]['importance']

        return "{} --> {}, Category:{}".format(ner,ner_score,ner_category)


    def Emotion(self,text):

        url = "https://api.edenai.run/v2/text/emotion_detection"

        payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "providers": "nlpcloud",
            "text": text
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFiMzFlOTktZWFmZS00YzZhLWJhZDAtMjQ3Y2ZkYjdiZGE0IiwidHlwZSI6ImFwaV90b2tlbiJ9.A2RKJHhsCWAj2p3jlfXarJPgPB3ZpAqoaPFqm5-jNTg"
        }

        response = requests.post(url, json=payload, headers=headers)

        ans = response.json()

        emotion = ans['nlpcloud']['items'][0]['emotion']
        emotion_rate = ans['nlpcloud']['items'][0]['emotion_score']

        return "{} --> {}".format(emotion,emotion_rate)
