import types
from packages.panels.manage_panels import ManagePanels 
import inspect

def config_function(cls, func) -> dict:
    sig = inspect.signature(func)
    parameter = sig.parameters
    func_parameters = {}
    func_name = func.__name__
    func_parameters[func_name] = {}
    for name, param in parameter.items():
        value = param.default if param.default != inspect._empty else "No Default Value"
        func_parameters[func_name][name] = value
    return func_parameters

def primeira_funcao(primeiro_parametro:str, segundo_parametro:int):
    """Exemplo de primeira função."""
    print("Primeira função executando...")

def segunda_funcao(outra_funcao, outro_parametro: any):
    outra_funcao()
    print('Segunda função executando...')


funcs_setup = ManagePanels('main')
funcs_setup.add_cmds('show menu', funcs_setup._printer, 'Mostra todos os comandos e funções disponíveis')
funcs_setup.add_cmds('config', config_function,'Configura a função selecionada')
funcs_setup.add_func('p2', segunda_funcao, 'Executa a função p2')
funcs_setup.run()