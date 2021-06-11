from audio_recg import speech2text, text2speech
import time
import pyperclip

def simple():
	while True:
		try:
			output = speech2text()
			print(output)
			pyperclip.copy(output)
			text2speech('did you say,' + output)
			time.sleep(2)
			print()
			text2speech('Your lines are copied')
			oncemore = 'If you would Like to try once more ..? \n Press Enter'
			print(oncemore)
			text2speech(oncemore)
			input()


		except KeyboardInterrupt:
			print('Closing speech2text ...')
			break

		except Exception as ex:
		    print(ex)
		    try_again = 'Please try again, I could not catch your words..'
		    print(try_again)
		    text2speech(try_again)
		    # print()

	input()

simple()
