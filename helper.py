import os
import time
from datetime import date
from datetime import datetime

import win32clipboard
from pynput.keyboard import Listener

import values


def get_clipboard_data():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    write_to_file(data)


def write_to_file(clipboard_data):
    import values
    temp = str(date.today()) + '.txt'
    filename = os.path.join(values.FILE_PATH, temp)
    cur_time = datetime.now()
    timestamp = cur_time.strftime("%H:%M:%S")

    # print(filename)

    with open(filename, 'a') as the_file:
        the_file.write(timestamp + ": " + clipboard_data + "\n\n")


def on_press(key):
    # print('{0} pressed'.format(key))
    if key in values.COMBINATION:
        time.sleep(0.6)
        get_clipboard_data()


def validate_path(file_path):
    if os.path.exists(file_path):
        return True
    return False


def create_file_loc():
    if not validate_path(values.FILE_PATH):
        os.makedirs(values.FILE_PATH, 777)


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()
