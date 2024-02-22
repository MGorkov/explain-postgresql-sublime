import urllib.request

class No302HTTPErrorProcessor(urllib.request.HTTPErrorProcessor):

	def http_response(self, request, response):
		code, msg, hdrs = response.code, response.msg, response.info()

		if (code == 302):
			return response

		# According to RFC 2616, "2xx" code indicates that the client's
		# request was successfully received, understood, and accepted.
		if not (200 <= code < 300):
			response = self.parent.error(
				'http', request, response, code, msg, hdrs)

		return response

	https_response = http_response

opener = urllib.request.build_opener(No302HTTPErrorProcessor)
urllib.request.install_opener(opener)
