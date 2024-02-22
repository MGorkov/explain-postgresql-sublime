import sublime

store = None

def load_plugin_settings():
	global store
	store = sublime.load_settings("Explain PostgreSQL.sublime-settings")

def get_plugin_settings(s):
	if (store.has(s)):
		return store.get(s)
	else:
		return None