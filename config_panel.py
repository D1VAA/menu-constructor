from typing import Callable
from packages.bcolors import Colors
from packages.panels.manage_panels import ManagePanels 
from time import sleep
import inspect

class ConfigPanel(ManagePanels):
    def setup(self, func):
        super().__init__('use')
        input_format = f'{self.panel} ({Colors.RED}{func.__name__}{Colors.RESET})>'
        self.func = func

        self._params = self._parameters()
        [self.add_opts(param, desc=value) for param, value in self._params.items()]
        self.add_cmds('show options', self.printer, 'Mostra esse menu')
        self.add_cmds('set', self._update_parameters, 'Configura os valores dos parâmetros.')
        self.add_cmds('run', self._execute, 'Roda a função')
        self.run(input_format=input_format)

    def _parameters(self):
        sig = inspect.signature(self.func)
        parameter = sig.parameters
        params = {}
        for name, param in parameter.items():
            value = param.default if param.default != inspect._empty else None
            params[name] = value
        return params
    
    def _update_parameters(self, parameter, new_value):
        if parameter not in self.opts_keys:
            print(f"{Colors.RED}[!]{Colors.RESET} Parâmetro não encontrado...")
            return
        elif ':' in new_value and new_value.split(':')[0] in self.instances.keys():
            ref, opt = new_value.split(':')
            print(f'\n\n{Colors.BLUE}[+]{Colors.RESET} Relative reference found >>>', end=' ')
            print(f'{Colors.RED}[Panel]{Colors.RESET} : {ref}\t{Colors.RED}[Opt]{Colors.RESET} : {opt}')
            sleep(0.3)
            instance = self.instances[ref]
            ref_opt = instance.opts[opt]['func']
            if ref_opt.__name__ == self.func.__name__:
                print(f"\n{Colors.RED}[!]{Colors.RESET} Invalid operation...\n")
                return
            self._params[parameter] = ref_opt

        else: 
            self._params[parameter] = new_value
        
        # Update and call the printer method
        self.opts[parameter]['desc'] = new_value
        self.printer(opt='opts')
    
    def _execute(self):
        print(f'{Colors.BLUE}[-]{Colors.RESET} Running...\n\n')
        self.func(**self._params)

main = ManagePanels('main')
usePanel = ConfigPanel('use')
main.add_cmds('show options', main.printer, 'Mostra todos os comandos e funções disponíveis')
main.add_cmds('use', usePanel.setup, 'Seleciona a função selecionada')
main.run()