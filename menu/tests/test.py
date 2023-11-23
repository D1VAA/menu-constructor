import unittest
from unittest.mock import patch
from src.manage_panels import ManagePanels
from src.config_panel import ConfigPanel
#from menu_builder import MenuBuilder

def example(um=None, dois=None):
    return 'Testing'

# Manage Panels test
panel_name = 'test_panel'

class TestManagePanels(unittest.TestCase):
    def setUp(self):
        self.manage_panels_instance = ManagePanels(panel_name)

    def test_manage_panels_creation(self):
        self.assertEqual(self.manage_panels_instance.panel, panel_name)
        self.assertEqual(self.manage_panels_instance.opts, {})
        self.assertEqual(self.manage_panels_instance.cmds, {})
        self.assertEqual(self.manage_panels_instance.opts_keys, set())
        self.assertEqual(self.manage_panels_instance.cmds_keys, set())

    def test_add_opts(self):
        self.manage_panels_instance.add_opts('option1', lambda x: x + 1, desc="Descrição option 1")
        self.assertIn('option1', self.manage_panels_instance.opts_keys)
        self.assertEqual(self.manage_panels_instance.opts['option1']['desc'], "Descrição option 1")
        self.assertEqual(self.manage_panels_instance.opts['option1']['func'](1), 2)

    def test_add_cmds(self):
        self.manage_panels_instance.add_cmds('command1', example, "Descrição comando 1")
        self.assertIn('command1', self.manage_panels_instance.cmds_keys)
        self.assertEqual(self.manage_panels_instance.cmds['command1']['desc'], "Descrição comando 1")
        self.assertEqual(self.manage_panels_instance.cmds['command1']['func'](), 'Testing')

class TestConfigPanelInstance(unittest.TestCase):
    def test_config_panel_instance(self, mock_input):
        test_case = ['set um 1', 'set dois 2']
        for case in test_case:
            self.config_panel_instance = ConfigPanel(panel_name).use(example, case)
        self.assertEqual(self.config_panel_instance.func_name, 'example')
        self.assertEqual(self.config_panel_instance._params['um'], '1')
        self.assertEqual(self.config_panel_instance._params['dois'], '2')

if __name__ == '__main__':
    unittest.main()
