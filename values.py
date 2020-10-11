from pynput import keyboard


class Values:
    def __init__(self):
        self.COMBINATION = {keyboard.KeyCode.from_char('\x03')}
        self.DEFAULT_PATH = 'C:\\Clipboard-log\\'
        self.FILE_PATH = 'C:\\Clipboard-log\\'
        self.PATH_NOT_ALLOWED = {'C:', 'C:\\', 'C:\\\\', 'C:/', 'C://'}

    def update_filepath(self, path):
        self.FILE_PATH = path
        print('File path updated to: ' + self.FILE_PATH)

    def reset_filepath_to_default(self):
        self.FILE_PATH = self.DEFAULT_PATH
        print('File path reset to: ' + self.FILE_PATH)

    def get_combo(self):
        return self.COMBINATION

    def get_default_path(self):
        return self.DEFAULT_PATH

    def get_file_path(self):
        return self.FILE_PATH

    def get_path_not_allowed(self):
        return self.PATH_NOT_ALLOWED
