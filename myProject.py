import speech_recognition as sr

recog = sr.Recognizer()



myAudio = sr.AudioFile('New.wav')
with myAudio as source:
    audio = recog.record(source)
    
recog.recognize_google(audio)