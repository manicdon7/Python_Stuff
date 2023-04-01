import os
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

# define a function to extract audio features
def extract_features(file_path):
    [sampling_rate, signal] = audioBasicIO.read_audio_file(file_path)
    features = ShortTermFeatures.feature_extraction(signal, sampling_rate, 0.050*sampling_rate, 0.025*sampling_rate)
    return features

# initialize speech recognizer
listener = sr.Recognizer()

# record audio from microphone
with sr.Microphone() as source:
    print("Please Speak Now")
    engine.say("Please speak now")
    engine.runAndWait()
    wav = listener.record(source, duration=5)
    
# save recorded audio to file
file_path = "audio.wav"
with open(file_path, "wb") as f:
    f.write(wav.get_wav_data())

# extract features from the audio file
features = extract_features(file_path)

# check if pitch and volume features are present in the extracted features
if len(features[1]) > 0 and len(features[0]) > 0:
    # extract pitch and volume features from the extracted features
    pitch = features[1][0]
    volume = features[0][0]

    # determine mood based on pitch and volume
    if ord(pitch[0]) > 150 and volume[0] > 0.01:
        print("The person may be happy or excited.")
        engine.say("The person may be happy or excited.")
        engine.runAndWait()
        
    elif ord(pitch[0]) > 100 and volume[0] > 0.01:
        print("The person may be sad or depressed.")
        engine.say("The person may be sad or depressed.")
        engine.runAndWait()
    else:
        print("The person's mood is difficult to determine.")
        engine.say("The person's mood is difficult to determine.")
        engine.runAndWait()
else:
    print("Could not extract pitch and volume features from the audio.")
    engine.say("Could not extract pitch and volume features from the audio.")
    engine.runAndWait()
    
    
