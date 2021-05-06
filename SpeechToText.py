import speech_recognition as sr

def SpeechToTextConversion(audiofile):

    recog = sr.Recognizer()

    with sr.AudioFile(audiofile) as source:
        audio = recog.record(source)

    try:
        textdata = recog.recognize_google(audio)
        print("Text data: " + textdata)
        return textdata

    except sr.UnknownValueError:
        print(" Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))