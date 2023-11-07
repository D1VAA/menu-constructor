from ..bcolors import Colors
from ..functions.manage_functions import ManageFunctions

class ManagePanels(ManageFunctions):
    _instances = {}
    def __init__(self, panel:str):
        self.panel_data = {}
        self.panel = str(panel)
        self.panel_data = {'funcs': {}, 'cmds': {}}
    
    def __new__(cls, *args, **kwargs):
        panel = args[0] if args else kwargs.get('panel')
        if panel in cls._instances:
            return cls._instances[panel]
        new_instance = super(ManagePanels, cls).__new__(cls)
        cls._instances[panel] = new_instance
        return new_instance

    def add_func(self, nick, func: object, desc = None) -> dict:
        self.panel_data['funcs'][nick] = {'func': func, 'desc': str(desc)}

    def add_cmds(self, nick, func, desc: str = None):
        self.panel_data['cmds'][nick] = {'func': func, 'desc': str(desc)}
    
    def _printer(self, opt=None):
        if opt is None:
            print(f'{"=" * 25} COMANDOS {"=" * 25}', end='\n\n')
            commands = self.panel_data['cmds']
            functions = self.panel_data['funcs']
            for nick, infos in commands.items():
                description = infos['desc']
                print(f'{Colors.RED}[-] {nick} {Colors.YELLOW}>{Colors.RESET} {description}', end='\n')
            print(f'\n{"=" * 25} FUNÇÕES {"=" * 25}', end='\n\n')
            for nick, infos in functions.items():
                description = infos['desc']
                print(f'{Colors.CIAN}[+] {nick} {Colors.YELLOW}>{Colors.RESET} {description}', end='\n')
            print('\n\n')
        elif opt is not None: 
            return

    def run(self, input_format=None):
        self._printer()
        cmds = self.panel_data['cmds']
        funcs = self.panel_data['funcs']
        df_format = f'({Colors.RED}{self.panel}{Colors.RESET})>' if input_format is None else input_format
        while True:
            opt = input(f'{df_format} ')
            try:
                if opt not in cmds.keys():
                        if opt in ['exit', 'quit']:
                            break
                        cmd = opt.split()[0]
                        args = opt.split()[1:] 
                        
                        # Replace the nick with the function obj
                        for i, x in enumerate(args):
                            if x in funcs.keys():
                                args[i] = funcs[x]['func']
                        cmds[cmd]['func'](*args)
                else:
                    cmds[opt]['func']()

            except Exception as e:
                print(f'{Colors.RED}[!] ERROR >>> {Colors.RESET}', str(e))