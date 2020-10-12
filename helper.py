import time
from datetime import date
from datetime import datetime

import win32clipboard
from pynput import keyboard
from pynput.keyboard import Listener

from settings import get_path

COMBINATION = {keyboard.KeyCode.from_char('\x03')}


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
    filename = get_path() + '\\' + temp
    print(filename)
    cur_time = datetime.now()
    timestamp = cur_time.strftime("%H:%M:%S")

    with open(filename, 'a') as the_file:
        the_file.write(timestamp + ": " + clipboard_data + "\n\n")


def on_press(key):
    # print('{0} pressed'.format(key))
    if key in COMBINATION:
        sleep_wait(0.6)
        get_clipboard_data()


def sleep_wait(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()
