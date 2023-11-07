import types
from packages.bcolors import Colors
from packages.panels.manage_panels import ManagePanels 
import inspect

class ManagePanelsWithConfig(ManagePanels):
    def config_function(self, func) -> dict:
        sig = inspect.signature(func)
        parameter = sig.parameters
        func_parameters = {}
        func_name = func.__name__
        func_parameters[func_name] = {}
        for name, param in parameter.items():
            value = param.default if param.default != inspect._empty else "No Default Value"
            func_parameters[func_name][name] = value
        while True:
            cmd = str(input(f'use ({Colors.HARD_RED}{func.__name__}{Colors.RESET})> '))
            if cmd in ['exit', 'quit']:
                return


def primeira_funcao(primeiro_parametro:str, segundo_parametro:int):
    """Exemplo de primeira função."""
    print("Primeira função executando...")

def segunda_funcao(outra_funcao, outro_parametro: any):
    outra_funcao()
    print('Segunda função executando...')


funcs_setup = ManagePanelsWithConfig('main')
funcs_setup.add_cmds('show menu', funcs_setup._printer, 'Mostra todos os comandos e funções disponíveis')
funcs_setup.add_cmds('use', funcs_setup.config_function,'Seleciona a função selecionada')
funcs_setup.add_func('p1', primeira_funcao, 'Executa a função p2')
funcs_setup.add_func('p2', segunda_funcao, 'Executa a função p2')
funcs_setup.run()