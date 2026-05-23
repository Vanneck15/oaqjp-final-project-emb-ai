import requests

def emotion_detector(text_to_analyze):
    # Enregistrer l'URL et les en-têtes fournis
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Créer le dictionnaire JSON d'entrée avec la variable text_to_analyze
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Envoyer la requête POST
    response = requests.post(url, json=input_json, headers=headers)
    
    # Renvoyer l'attribut text de la réponse comme demandé
    return response.text