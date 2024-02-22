from html.parser import HTMLParser

class OGHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.data = ""

	def handle_starttag(self, tag, attrs):
		if (tag == 'meta' and attrs[0][1] == 'og:image'):
			self.data = attrs[1][1]

parser = OGHTMLParser()
