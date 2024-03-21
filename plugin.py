from .commands import *
from .utils import check_deps

def plugin_loaded():
	check_deps()
