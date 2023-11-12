from menu.utils import Colors
from src.manage_panels import ManagePanels 
from src.modules.class_handler import Setup
from time import sleep
import inspect

class ConfigPanel(ManagePanels, Setup):
    """
    This class uses some resources from the ManagePanels class, to make a Panel that allow the user 
    to configurate parameters and execute functions that were added as an [opt].
    """
    def use(self, obj):
        Setup.__init__(self, obj)
        # Use Panel Setup
        self.use = ManagePanels('use')
        input_format = f'{self.use.panel} ({Colors.RED}{obj.__name__}{Colors.RESET})>'
        self.func = obj 

        self._params = self.get_parameters
        [self.use.add_opts(param, desc=value) for param, value in self._params.items()]
        self.use.add_cmds('show options', self.printer, 'Mostra esse menu')
        self.use.add_cmds('set', self._update_parameters, 'Configura os valores dos parâmetros.')
        self.use.add_cmds('run', self._execute, 'Roda a função')
        self.use.run(input_format=input_format)
    
    def _update_parameters(self, parameter, new_value):
        # Method used to update the parameters values
        if parameter not in self.use.opts_keys:
            print(f"{Colors.RED}[!]{Colors.RESET} Parâmetro não encontrado...")
            return
        # Relative reference = pass another function as a value for the parameter (like "panel_name:function_nick")
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
        self.use.opts[parameter]['desc'] = new_value
        self.use.printer(opt='opts')
    
    def _execute(self):
        print(f'{Colors.BLUE}[-]{Colors.RESET} Running...\n\n')
        self.func(**self._params)
