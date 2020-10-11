import os
import time
from datetime import date
from datetime import datetime

import win32clipboard
from pynput.keyboard import Listener

import values

all_values = values.Values()


def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        # print(type(data))
        win32clipboard.CloseClipboard()
        write_to_file(data)

    except TypeError:
        # if data is not textual
        win32clipboard.CloseClipboard()


def write_to_file(clipboard_data):
    temp = str(date.today()) + '.txt'
    filename = all_values.get_file_path() + '\\' + temp
    # print(filename)
    cur_time = datetime.now()
    timestamp = cur_time.strftime("%H:%M:%S")

    with open(filename, 'a') as the_file:
        the_file.write(timestamp + ": " + clipboard_data + "\n\n")


def on_press(key):
    # print('{0} pressed'.format(key))
    if key in all_values.get_combo():
        sleep_wait(0.6)
        get_clipboard_data()


def sleep_wait(seconds):
    time.sleep(seconds)


def validate_path(file_path):
    if file_path in all_values.get_path_not_allowed():
        print('Permission denied! Please choose another location.')
        return False
    if os.path.isdir(file_path):
        return True
    return False


def create_file_loc():
    if not validate_path(all_values.get_file_path()):
        os.makedirs(all_values.get_file_path(), 777)


def update_settings():
    pass


# if __name__ == '__main__':
def main():
    with Listener(on_press=on_press) as listener:
        listener.join()
