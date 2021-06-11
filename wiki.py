import audio_recg, wikipedia

def wiki():	
	try:
		topic = 'What do you want to know about ..?'
		print(topic)
		audio_recg.text2speech(topic)
		output = audio_recg.speech2text()
		# words = output.split()
		# del words[:3]
		# words = ' '.join(words)
		print('\n',"Please wait ...",end='\r')

		data = wikipedia.summary(output, sentences = 3)

		print('About',output,':')
		audio_recg.text2speech("here is something about"+output)
		print(data)
		audio_recg.text2speech(data)
		

	except Exception as ex:
		print(ex)
		try_again = 'Please try again, I could not catch your words..'
		print(try_again)
		audio_recg.text2speech(try_again)
		wiki()

wiki()
input()