from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask('Emotions Detector')

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    emotion_to_detect = request.args.get('textToAnalyze')

    response = emotion_detector(emotion_to_detect)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return "The given emotion has been identified as {} with a score of {}.".format(dominant_emotion, joy)

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)



