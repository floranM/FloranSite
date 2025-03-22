from .base import *

DEBUG = False

try:
    from .local import * # type: ignore
except ImportError:
    pass
