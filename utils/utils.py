import sublime
import json
import urllib.request
import base64
import http
# http.client.HTTPConnection.debuglevel = 0
from .plugin_settings import *

TEMPLATE_HTML = """
<html><body>
<h3>Click image to open Explain PostgreSQL plan visualizer</h3>
<a href="{}">
	<img alt="click to open site" src="data:image/png:base64,{}"></img>
<a/>
</body></html>"""

ICON_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAdZJREFUKJGlkr9r01EUxT/3JWkqrUL1LxB0aVETv63SoYJTh4ylHZq0oEITiQoRBy2ClYo6KaiBfLuobVKHIC46iEOVIsUfsYNmFycXF20x+aZ516H9xhgJWDzT47x3zuG8e4UmRCdzg0blrsBywFavvCmc+w5wNH5nV92EryoMWdGzq/OpFV8jAEcm7+2p29BNhGFVuQQ6JBATa0cA1JjHCs9AlkX0BsrzgKldfDt/5pv0T+ROqco1hEKlsjFTLqbXAJxELoua8maM7SvlU2mAvtFsd2dncAYlLqKXg6riokRL+eTH5joi4qn+Pvv8VsAFJ+4+VGTVAPVS4U/xQHxuQJVhFfuTNtjS1E3rRXQ8d8yKPhF09kM+db+dgY9gK7Gvtvv1l46vvf4Etm1QLI7VgX8S+wbrTnxutsNbu75SPN+2czMGR2/t8Dq6p0HXjQlu9CJ2rxfu+uQk3BhsLk7/hJsBlVaxk3BjXrirjLGRoJqDjQfOuHscQ1bhs8ABVJ7uDIUyP2q1k2J0//uFZOZwwn0kcAhLurSYXAJoTKG0mFyqVHsiRngh1o6UClOnXz44UWlOD4jkKtWeiC/2/6CBcnHMA2636/5uYepVK/fXHmwX/23wC4oPtzpbGkUYAAAAAElFTkSuQmCC"

TEMPLATE_TEXT = '<a href="{}"><img src="data:image/png:base64,' + ICON_BASE64 + '"> Explain PostgreSQL plan visualizer</a>'

def check_deps():
	if ('Packages/SQLTools/package-metadata.json' not in sublime.find_resources('package-metadata.json')):
		sublime.error_message('"Explain PostgreSQL" plugin requires "SQLTools" plugin installed.')
		sublime.run_command('install_package')
		return False
	else:
		return True

def check_is_visible(view):
	syntax = view.settings().get("syntax")
	if (syntax.endswith("SQL.sublime-syntax")):
		return True
	else:
		return False

def send_post_request(url, data, parse=False):
	data = json.dumps(data).encode('utf-8')
	headers = {
		"Content-Type": "application/json; charset=utf-8",
		"Method": "POST"
	}
	try:
		req = urllib.request.Request(url, data, headers)
		with urllib.request.urlopen(req) as response:
			if (response.code == 302):
				return response.headers["Location"]
			response_data = response.read().decode('utf-8')
			if (parse):
				return json.loads(response_data)
			else:
				return response_data
	except Exception as e:
		print(e)

def show_popup(view, content):
	# view.show_popup(content, flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY, max_width=600, max_height=600)
	view.show_popup(content, max_width=600, max_height=600)

def get_explain_cmd():
	s = []
	explain = get_plugin_settings("explain")
	for key in explain.keys():
		if (explain[key]): s.append(key)
	return "EXPLAIN ({}) ".format(','.join(s))

def get_html(url):
	try:
		req = urllib.request.Request(url, method='GET')
		with urllib.request.urlopen(req, timeout=30) as response:
			return response.read()
	except Exception as e:
		print(e)

def encode_img(img):
	return base64.b64encode(img).decode("utf-8")

def get_img_html(url, img_encoded):
	return TEMPLATE_HTML.format(url, img_encoded)

def get_text_html(url):
	return TEMPLATE_TEXT.format(url)