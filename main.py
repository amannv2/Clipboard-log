import os
import subprocess
from winreg import OpenKey, KEY_ALL_ACCESS, HKEY_CURRENT_USER, SetValueEx, REG_SZ

import win32api
import win32event
import winerror

import helper
import settings


# Add to startup
def add_to_startup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = 'main.py'
    new_file_path = fp + "\\" + file_name
    key_val = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = OpenKey(HKEY_CURRENT_USER, key_val, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "Clipboard log", 0, REG_SZ, new_file_path)


if __name__ == '__main__':

    print('\n*********Welcome to Clipboard log*********\n')

    if settings.first_launch():
        while True:
            print('Default location is C:\\Clipboard-log')
            path = input('\nPlease enter a location for storing logs (Press enter to use default location): ')

            if path == '' or settings.validate_path(path):
                if not path == '':
                    settings.update_path(path)
                else:
                    print('Using default location.\n')
                break
            print('Invalid path!')

        if input('Add this program to the startup(y/n)?').lower() == 'y':
            print('Added to program to the startup.\n')
            add_to_startup()

        # create installation dir
        settings.create_file_loc()

        # install dependencies
        print('\nInstalling dependencies...Please make sure your Python version is >= 3.9.0\n')
        helper.sleep_wait(2)
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

        settings.update_first_launch()
    else:
        print('Current location for Clipboard logs is: ' + settings.get_path())

    # limit to single instance
    mutex = win32event.CreateMutex(None, 1, 'mutex_var_clip-log')
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        mutex = None
        input('\nMultiple Instances not Allowed! Exiting...')
        exit(0)

    input('Press Enter to continue')
    helper.hide()
    helper.main()
    # os.startfile('helper.py')
    # start running in background
    # DETACHED_PROCESS = 8
    # subprocess.Popen("python helper.py", creationflags=DETACHED_PROCESS, close_fds=True)
