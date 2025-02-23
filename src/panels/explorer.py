import os

from src.panels.base_panel import BasePanel


class ExplorerPanel(BasePanel):

    def controller(self, stdscr):
        # listen to key inputs
        pass

    def display(self, stdscr):
        # display ui
        pass

    def list_files(self, directory):
        """Returns a list of files and folders in the given directory."""
        try:
            return (
                os.listdir(directory)
                if os.listdir(directory)
                else ["(empty directory)"]
            )
        except PermissionError:
            return ["(permission denied)"]


def display_windows(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    if height < 10 or width < 40:
        stdscr.addstr(1, 1, "Terminal too small. Resize and restart.")
        stdscr.refresh()
        stdscr.getch()
        return

    left_win_width = width // 3
    right_win_width = width - left_win_width - 3

    left_win = curses.newwin(height - 2, left_win_width, 1, 1)
    right_win = curses.newwin(height - 2, right_win_width, 1, left_win_width + 2)

    left_win.box()
    right_win.box()

    current_dir = os.getcwd()
    files = list_files(current_dir)
    selected_index = 0

    # left_win.refresh()
    # right_win.refresh()
    stdscr.refresh()

    while True:
        left_win.clear()
        left_win.box()
        right_win.clear()
        right_win.box()

        for i, file in enumerate(files):
            if i == selected_index:
                left_win.attron(curses.A_REVERSE)
                left_win.addstr(i + 1, 2, file)
                left_win.attroff(curses.A_REVERSE)
            else:
                left_win.addstr(i + 1, 2, file)

        selected_file = (
            os.path.join(current_dir, files[selected_index])
            if files and files[0] not in ["(empty directory)", "(permission denied)"]
            else None
        )
        if selected_file and os.path.isfile(selected_file):
            try:
                with open(selected_file, "r", errors="ignore") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines[: height - 4]):
                    right_win.addstr(i + 1, 2, line[: right_win_width - 3])
            except Exception as e:
                right_win.addstr(1, 2, f"Error reading file: {str(e)}")

        left_win.refresh()
        right_win.refresh()

        key = stdscr.getch()
        if (key == curses.KEY_UP or key == ord("k")) and selected_index > 0:
            selected_index -= 1
        elif (key == curses.KEY_DOWN or key == ord("j")) and selected_index < len(
            files
        ) - 1:
            selected_index += 1
        elif key == ord("q"):
            break
