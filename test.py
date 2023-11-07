import types
from packages.panels.manage_panels import ManagePanels 
import inspect

def config_function(cls, func) -> dict:
    func = cls.panel_data[cls.panel_name]['funcs'][cls.nick]
    sig = inspect.signature(func)
    parameter = sig.parameters
    func_name = func.__name__
    cls.func_parameters[func_name] = {}
    for name, param in parameter.items():
        value = param.default if param.default != inspect._empty else "No Default Value"
        cls.func_parameters[func_name][name] = value
    return cls.func_parameters

def primeira_funcao(primeiro_parametro:str, segundo_parametro:int):
    """Exemplo de primeira função."""
    print("Primeira função executando...")

def segunda_funcao(outra_funcao, outro_parametro: any):
    outra_funcao()
    print('Segunda função executando...')


funcs_setup = ManagePanels('main')
funcs_setup.config_function = types.MethodType(config_function, funcs_setup)
funcs_setup.add_cmds('show menu', funcs_setup._printer, 'Mostra todos os comandos e funções disponíveis')
funcs_setup.add_cmds('config', funcs_setup.config_function,'Configura a função selecionada')
funcs_setup.add_func('p2', segunda_funcao, 'Executa a função p2')
funcs_setup.run()