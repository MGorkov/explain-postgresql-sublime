from .commands import *
from .utils import check_deps,load_plugin_settings

def plugin_loaded():
	check_deps()
	load_plugin_settings()
