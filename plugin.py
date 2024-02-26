from .commands import *
from .utils import load_plugin_settings

def plugin_loaded():
	load_plugin_settings()
