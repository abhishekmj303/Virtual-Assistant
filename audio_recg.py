import pyttsx3
import speech_recognition as sr

def text2speech(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(str(text))
	engine.runAndWait()
	engine.stop()

def speech2text():
	r = sr.Recognizer()
	mic=sr.Microphone()

	with mic as source:
		#r.adjust_for_ambient_noise(source)
		print("Start Speaking... ")
		#text2speech("Start Speaking")
		audio=r.listen(source)

	text = r.recognize_google(audio)
	return text
