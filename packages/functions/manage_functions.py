import inspect

class ManageFunctions:
    func_parameters = {}
    @classmethod
    def config_function(cls, nick: str, func, desc: str = None) -> dict:
        sig = inspect.signature(func)
        parameter = sig.parameters
        func_name = func.__name__
        cls.func_parameters[func_name] = {}
        for name, param in parameter.items():
            value = param.default if param.default != inspect._empty else "No Default Value"
            cls.func_parameters[func_name][name] = value
