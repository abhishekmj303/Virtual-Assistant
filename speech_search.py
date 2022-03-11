from audio_recg import speech2text#, text2speech
import time
import pyperclip
import webbrowser
import urllib.parse

def simple():
    run = 1
    while True:
        try:
            if run == 1:
                output = speech2text()
                run = 0
                print()
                print(output)
                pyperclip.copy(output)
                # text2speech('did you say,' + output)
                time.sleep(2)
                print()
                print('Your lines are copied')
                # oncemore = 'If you would Like to try once more ..? \n Press Enter'
                # print(oncemore)
                # text2speech(oncemore)
                input('Press ENTER to search on Whoogle ... ')
                output_url = urllib.parse.quote_plus(output)
                # output_url = output.split()
                # output_url = '+'.join(output_url)
                url = 'https://search.mj303.live/search?q=' + output_url
                webbrowser.open_new_tab(url)

            else:
                break


        except KeyboardInterrupt:
            print('Closing speech2text ...')
            run = 0
            break

        except Exception as ex:
            print(ex)
            run = 1
            try_again = 'Please try again, I could not catch your words..'
            print(try_again)
            #text2speech(try_again)
            # print()

    # input()

simple()
