import audio_recg, pygetwindow as gw

def close(app):
    if app != '':
        gw.getWindowsWithTitle(app)[0].close()

def close_app():
	try:
		command = audio_recg.speech2text()
		app = command.split()[1:]
		app = ' '.join(app)
		print('Closing',app)
		#audio_recg.text2speech('Closing '+app)
		close(app)
		
	except Exception as ex:
		print(ex)
		try_again = 'Something went wrong. Please try again...'
		print(try_again)
		#audio_recg.text2speech(try_again)
		close_app()

close_app()