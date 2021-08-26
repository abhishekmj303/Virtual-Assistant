import pyperclip, webbrowser, urllib.parse, os

try:
	data = pyperclip.paste().strip()
	print('Your clipboard contains : ', data)
	print()

	try:
		if (data[0]=='"' and data[-1]=='"') or (data[0]=="'" and data[-1]=="'"):
			data = data[1:-1].strip()

	except Exception as ex:
		print('Nothing to do')
		exit(input('Your clipboard is empty'))

	if data == '':
		print('Nothing to do')
		exit(input('Your clipboard is empty'))

	urls = ['https://', 'http://', 'ftp://']

	if (data[:8] in urls) or (data[:7] in urls) or (data[:6] in urls):
		print('Opening', data, '...')
		webbrowser.open_new_tab(data)

	elif (data[1:3] or data[2:4]) == ':\\':
		# data = '"'+data+'"'
		print('Opening "'+data+'" ...  ')
		os.startfile(os.path.realpath(data))

	else:
		print('Searching Google for "'+data+'"')
		url_parse = urllib.parse.quote_plus(data)
		webbrowser.open_new_tab('https://google.com/search?q='+url_parse)

except Exception as ex:
	print(ex)
	input()