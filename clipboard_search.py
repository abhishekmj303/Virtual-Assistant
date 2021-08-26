import pyperclip, webbrowser, urllib.parse, os

try:
	data = pyperclip.paste().strip()
	print('Your clipboard contains : ', data)
	print()
	if data[0]=='"' and data[-1]=='"':
		data = data[1:-1]
	urls = ['https://', 'http://', 'ftp://']

	if urls in data[:8]:
		print('Opening', data, '...')
		webbrowser.open_new_tab(data)

	elif (data[1:3] or data[2:4]) == ':\\':
		# data = '"'+data+'"'
		print('Opening "'+data+'" ...  ')
		os.startfile(os.path.realpath(data))

	elif data == '':
		print('This data type is not supported')
		print('Please copy any "Text" or "Url"')
		input()

	else:
		print('Searching Google for "'+data+'"')
		url_parse = urllib.parse.quote_plus(data)
		webbrowser.open_new_tab('https://google.com/search?q='+url_parse)

except Exception as ex:
	print(ex)
	input()