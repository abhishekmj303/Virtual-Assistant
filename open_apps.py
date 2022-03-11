import audio_recg, pyautogui as bot, time

def open(app):
	bot.hotkey('alt','space')
	time.sleep(1)
	bot.write(app)
	time.sleep(1)
	bot.press('enter')

def open_app():
	try:
		command = audio_recg.speech2text()
		app = command.split()[1:]
		app = ' '.join(app)
		print('Opening',app)
		#audio_recg.text2speech('Opening '+app)
		open(app)
		
	except Exception as ex:
		print(ex)
		try_again = 'Something went wrong. Please try again...'
		print(try_again)
		#audio_recg.text2speech(try_again)
		open_app()

open_app()
