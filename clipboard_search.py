import pyperclip, urllib.parse, subprocess

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
	fileSystem = ['~/', '/bin', '/boot', '/cdrom', '/dev', '/etc', '/home', '/lib', '/lib32', '/lib64',
		'/libx32', '/media', '/mnt', '/opt', '/proc', '/root', '/run', '/sbin', '/snap', '/srv',
		'/sys', '/tmp', '/usr', '/var']
	xdgOpen = False

	for i in range(2,9):
		if data[:i] in fileSystem:
			xdgOpen = True

		elif i>=6 and i<=8:
			if data[:i] in urls:
				xdgOpen = True

	if xdgOpen==True:
		print("Opening ", data, "...")
		subprocess.run(["xdg-open", data])

	else:
		print('Searching Google for "'+data+'"')
		url_parse = urllib.parse.quote_plus(data)
		data = 'https://search.mj303.live/search?q='+url_parse
		subprocess.Popen(['xdg-open', data])

except Exception as ex:
	print(ex)
	input()