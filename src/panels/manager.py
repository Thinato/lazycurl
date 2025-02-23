from src.panels.base_panel import BasePanel
from src.panels.editor import EditorPanel
from src.panels.environment import EnvironmentPanel
from src.panels.explorer import ExplorerPanel
from src.panels.history import HistoryPanel
from src.panels.settings import SettingsPanel


class PanelManager:
    focused_panel: BasePanel

    editor: EditorPanel
    environment: EnvironmentPanel
    explorer: ExplorerPanel
    history: HistoryPanel
    settings: SettingsPanel

    def __init__(self, explorer, editor, environment, history, settings):
        self.explorer = explorer
        self.editor = editor
        self.environment = environment
        self.history = history
        self.settings = settings
