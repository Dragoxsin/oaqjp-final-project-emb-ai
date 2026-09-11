from .emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):

    anger_result = emotion_detector["I am really mad about this"]
    self.assertEqual(anger_result['emotion' 'anger'])

    disgust_result = emotion_detector["I feel disgusted just hearing about this"]
    self.assertEqual(disgust_result['emotion' 'disgust']) 

    fear_result = emotion_detector["I am really afraid that this will happen"]
    self.assertEqual(fear_result['emotion' 'fear'])

    joy_result = emotion_detector["I am glad this happened"]
    self.assertEqual(joy_result['emotion' 'joy'])

    sadness_result = emotion_detector["I am so sad about this"]
    self.assertEqual(sadness_result['emotion' 'sadness'])

unittest.main()

