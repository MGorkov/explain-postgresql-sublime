import sublime

def get_plugin_settings(s):
	return sublime.load_settings("Explain PostgreSQL.sublime-settings").get(s)
