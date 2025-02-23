import argparse

from src.config import Config
from src.panels.editor import EditorPanel
from src.panels.environment import EnvironmentPanel
from src.panels.explorer import ExplorerPanel
from src.panels.history import HistoryPanel
from src.panels.manager import PanelManager
from src.panels.settings import SettingsPanel


def main():
    parser = argparse.ArgumentParser(
        prog="lazycurl",
        description="cURL with a pretty interface.",
        epilog="Made by Thinato.",
    )
    parser.add_argument("-c", "--config", help="Path to the configuration directory.")
    args = parser.parse_args()

    config = Config(args.config)

    # dependency injection here

    explorer_panel = ExplorerPanel()
    editor_panel = EditorPanel()
    environment_panel = EnvironmentPanel()
    history_panel = HistoryPanel()
    settings_panel = SettingsPanel()

    panel_manager = PanelManager(
        explorer_panel, editor_panel, environment_panel, history_panel, settings_panel
    )

    panel_manager.focused_panel = panel_manager.explorer

