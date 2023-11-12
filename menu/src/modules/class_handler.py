import inspect
from menu.panels.config_panel import ConfigPanel

class Setup:
    """Class to verify the data before pass to the config panel"""
    def __init__(self, obj):
        self.obj = obj

    @property
    def isclass(self) -> bool:
        return inspect.isclass(self.obj)
    
    @staticmethod
    def get_params(self) -> dict:
        sig = inspect.signature(self.obj.__init__) if self.isclass else inspect.signature(self.obj)
        init_params = sig.parameters
        params = {}
        for param, value in init_params.items():
            params[param] = value
        return params