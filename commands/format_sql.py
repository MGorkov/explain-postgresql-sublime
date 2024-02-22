import sublime
import sublime_plugin

from ..utils import *

BEATIFIER_API="/beautifier-api"

class EpFormatSqlCommand(sublime_plugin.TextCommand):
	def is_visible(self):
		return check_is_visible(self.view)

	def run(self, edit):
		v = self.view
		selection = v.sel()[0]
		if selection.empty():
			selection = sublime.Region(0, v.size())
			text = v.substr(selection)
		else:
			text = v.substr(selection)
		data = {"query_src": text}
		url = get_plugin_settings("api_url") + BEATIFIER_API
		res = send_post_request(url, data, True)
		if res['btf_query_text'] == res['btf_query']:
			show_popup(v, res['btf_query_text'])
		else:
			v.replace(edit, selection, res['btf_query_text'])
			sublime.status_message("Text formatted")
