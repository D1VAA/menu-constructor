import pytest
from menu.src import ManagePanels
from menu.src.config_panel import ConfigPanel
from menu.menu_builder import MenuBuilder
import inspect

def example(um=None, dois=None):
    return 'Testing'

#Manage Panels test
panel_name = 'test_panel'
@pytest.fixture
def manage_panels_instance():
    instance = ManagePanels(panel_name)
    return instance

def test_manage_panels_creation(manage_panels_instance):
    assert manage_panels_instance.panel == panel_name
    assert manage_panels_instance.opts == {}
    assert manage_panels_instance.cmds == {}
    assert manage_panels_instance.opts_keys == set()
    assert manage_panels_instance.cmds_keys == set()

def test_add_opts(manage_panels_instance):
    manage_panels_instance.add_opts('option1', lambda x: x+1, desc="Descrição option 1")
    assert 'option1' in manage_panels_instance.opts_keys
    assert manage_panels_instance.opts['option1']['desc'] == "Descrição option 1"
    assert manage_panels_instance.opts['option1']['func'](1) == 2

def test_add_cmds(manage_panels_instance):
    manage_panels_instance.add_cmds('command1', example, "Descrição comando 1")
    assert 'command1' in manage_panels_instance.cmds_keys
    assert manage_panels_instance.cmds['command1']['desc'] == "Descrição comando 1"
    assert manage_panels_instance.cmds['command1']['func']() == 'Testing'

@pytest.fixture
def config_panel_instance():
    instance = MenuBuilder(panel_name)
    return instance.use(example)

def test_config_panel_instance(config_panel_instance):
    return config_panel_instance
#     config_panel_instance = config_panel_instance.use(example)
#     assert config_panel_instance.func_name == 'example'
#     assert config_panel_instance.func_name in config_panel_instance.data
#     assert config_panel_instance._params == config_panel_instance.data[config_panel_instance.func_name]
#     assert 'um' in config_panel_instance._params and 'dois' in config_panel_instance._params
#     assert all(opt in config_panel_instance.opts_keys for opt in ['show options', 'set', 'run'])