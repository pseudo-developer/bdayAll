import speech_recognition as sr

#get audio from microphone
r= sr.Recognizer()
with sr.Microphone() as source:
    print("speak:")
    audio = r.listen(source)

#try
try:
    txt= r.recognize_google(audio)
    print("you said:",txt)
except sr.UnknownValueError:
    print("couldnot understand audio")
except sr.RequestError as e:
    print("couldnot request results; {0}".format(e))