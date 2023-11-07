import types
from packages.bcolors import Colors
from packages.panels.manage_panels import ManagePanels 
import inspect

class ManagePanelsWithConfig(ManagePanels):
    def config_function(self, func) -> dict:
        use = ManagePanels('use')
        self.func = func
        input_format = f'{use.panel} ({Colors.RED}{func.__name__}{Colors.RESET})>'
        use.add_cmds('help', use._printer, 'Mostra esse menu')
        use.add_cmds('show options', use.show_parameter, 'Mostra os parâmetros')
        use.run(input_format=input_format)

    def show_parameter(self):
        sig = inspect.signature(self.func)
        parameter = sig.parameters
        func_parameters = {}
        func_name = self.func.__name__
        func_parameters[func_name] = {}
        for name, param in parameter.items():
            value = param.default if param.default != inspect._empty else "No Default Value"
            func_parameters[func_name][name] = value
        print(func_parameters)

    def update_parameter(self, func, new_value):
        sig = inspect.signature(func)
        parameter = sig.parameters
        func_parameters = {}
        func_name = func.__name__
        func_parameters[func_name] = {}
        for name, param in parameter.items():
            value = param.default if param.default != inspect._empty else "No Default Value"
            func_parameters[func_name][name] = value

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