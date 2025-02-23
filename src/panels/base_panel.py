import abc


class BasePanel(abc.ABC):

    @abc.abstractmethod()
    def controller(self, stdscr):
        pass

    @abc.abstractmethod()
    def display(self, stdscr):
        pass
