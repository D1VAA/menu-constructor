from src.modules.class_handler import Setup
from src import ConfigPanel

class MenuBuilder(ConfigPanel):
    def __init__(self, panel):
        super().__init__(panel)

main = MenuBuilder('main')
main.add_cmds("show options", main.printer, 'Mostra')
main.add_cmds('use', main.use, 'Configura os parâmetros')
main.add_opts('p_config', ConfigPanel.use, 'Classe do painel de configurações')
main.run()