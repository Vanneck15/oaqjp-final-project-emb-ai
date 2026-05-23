import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test pour la joie (Je suis content que cela soit arrivé)
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test pour la colère (Je suis vraiment en colère à ce sujet)
        result_2 = emotion_detector("I am really angry about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test pour le dégoût (Je me sens dégoûté rien qu'en entendant parler de cela)
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Test pour la tristesse (Je suis si triste à ce sujet)
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # Test pour la peur (J'ai vraiment peur que cela arrive)
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()