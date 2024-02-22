import sublime
import sublime_plugin
import webbrowser
import SQLTools.SQLTools

from ..utils import *

EXPLAIN_API="/explain"
MSG_GETTING_PLAN="Getting plan..."

class EpExplainAnalyzeCommand(sublime_plugin.TextCommand):
	def is_visible(self):
		return check_is_visible(self.view)

	def run(self, edit):
		if (check_deps() == False): return
		ST = SQLTools.SQLTools.ST
		v = self.view
		selection = v.sel()[0]
		if selection.empty():
			selection = sublime.Region(0, v.size())
			text = v.substr(selection)
		else:
			text = v.substr(selection)

		def cb(result):
			data = {"query": text, "plan": result}
			api_url = get_plugin_settings("api_url")
			explain_api_url = api_url + EXPLAIN_API
			url = send_post_request(explain_api_url, data)
			plan_url = api_url + url
			show_link = get_plugin_settings("show_link")
			if (show_link in ["popup_diagram", 'newtab']):
				html = get_html(plan_url)
				parser.feed(html.decode("utf-8"))
				parser.close()
				bimg = get_html(parser.data)
				if (bimg == None): return
				b64img = encode_img(bimg)
				img_html = get_img_html(plan_url, b64img)
				if (show_link == 'newtab'):
					self.view.window().new_html_sheet("Explain Analyze", img_html) # , flags=sublime.TRANSIENT)
				else:
					show_popup(self.view, img_html)
			elif (show_link == 'browser'):
				webbrowser.open_new_tab(plan_url)
			elif (show_link == 'popup_text'):
				show_popup(self.view, get_text_html(plan_url))

		if not ST.conn:
			ST.selectConnectionQuickPanel(callback=lambda: sublime.active_window().run_command('ep_explain_analyze'))
			return

		args=ST.conn.buildArgs()
		args.append("-At")

		env=ST.conn.buildEnv()
		text = get_explain_cmd() + text
		v.window().status_message(MSG_GETTING_PLAN)

		ST.conn.Command.createAndRun(
			args=args,
			env=env,
			callback=cb,
			query=text,
			timeout=60,
			silenceErrors=True, # change to True
			stream=False
		)
