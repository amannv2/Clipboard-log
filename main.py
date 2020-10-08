import time
import win32clipboard
from datetime import date
from pynput import keyboard
from datetime import datetime
from pynput.keyboard import Listener


def get_clipboard_data():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    write_to_file(data)


def write_to_file(clipboard_data):
    filename = str(date.today()) + ".txt"
    cur_time = datetime.now()
    timestamp = cur_time.strftime("%H:%M:%S")

    with open(filename, 'a') as the_file:
        the_file.write(timestamp + ":\t" + clipboard_data + "\n\n")


COMBINATION = {keyboard.KeyCode.from_char('\x03')}
current = set()


def on_press(key):
    # print('{0} pressed'.format(key))
    if key in COMBINATION:
        time.sleep(0.6)
        get_clipboard_data()


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()
