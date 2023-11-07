from ..bcolors import Colors
from ..functions.manage_functions import ManageFunctions

class ManagePanels(ManageFunctions):
    _instances = {}
    def __init__(self, panel:str):
        self.panel_data = {}
        self.nick = None
        self.panel_data = {'funcs': {}, 'cmds': {}}
    
    def __new__(cls, *args, **kwargs):
        panel = args[0] if args else kwargs.get('panel')
        if panel in cls._instances:
            return cls._instances[panel]
        new_instance = super(ManagePanels, cls).__new__(cls)
        cls._instances[panel] = new_instance
        return new_instance

    def add_func(self, nick, func: object, desc = None) -> dict:
        self.nick = nick
        self.panel_data['funcs'][nick] = {'func': func, 'desc': str(desc)}
        return self.panel_data
    def add_cmds(self, nick, func, desc: str = None):
        self.panel_data['cmds'][nick] = {'func': func, 'desc': str(desc)}
        return self.panel_data
    
    def _printer(self, opt=None):
        print(self.panel_data['cmds'])
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
        elif opt is not None: 
            return
        
    def run(self):
        self._printer()
        while True:
            opt = str(input('> '))
            if len(opt.split()) > 1:
                cmd, f = opt.split()
                command = self.panel_data['cmds'][cmd]['func']
                func = self.panel_data['funcs'][f]['func']
            else:
                opt = self.panel_data['cmds'][f]['func']
            if opt.lower() == 'exit':
                break
