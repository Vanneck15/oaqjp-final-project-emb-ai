from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyse le texte fourni pour détecter les émotions et renvoie
    une chaîne de caractères formatée pour l'utilisateur.
    """
    # Récupérer le texte envoyé par le script JavaScript (mywebscript.js)
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Analyser le texte avec notre package EmotionDetection
    response = emotion_detector(text_to_analyze)
    
    # Extraire les scores et l'émotion dominante
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Retourner la chaîne de caractères EXACTEMENT au format attendu par le correcteur IBM
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Affiche la page d'accueil de l'application web.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Déploiement sur localhost (0.0.0.0) sur le port 5000
    app.run(host="0.0.0.0", port=5000)