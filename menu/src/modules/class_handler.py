import inspect
from typing import Optional, Type, Callable
from menu.src.config_panel import ConfigPanel

class Setup(ConfigPanel):
    """Class to support the ConfigPanel by handing with classes instead of functions"""
    def __init__(self, obj: Type, method: Optional[Callable] = None):
        self.obj = obj
        self._method = method
        self._init_params = self.obj_params(obj)
        self._method_params = self.obj_params(method) if method is not None else None