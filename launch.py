import webbrowser

PATH_TO_BROWSER = 'open -a /Applications/Google\ Chrome.app %s'

urls = ['https://mail.google.com', 'https://facebook.com', 'https://twitter.com', 'http://espn.go.com']

if __name__ == '__main__':
	for url in urls:
		webbrowser.get(PATH_TO_BROWSER).open(url)