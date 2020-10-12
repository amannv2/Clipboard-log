import subprocess

import helper
import settings

if __name__ == '__main__':

    print('\n*********Welcome to Clipboard log*********\n')

    if settings.first_launch():
        while True:
            print('Default location is C:\\Clipboard-log')
            path = input('\nPlease enter a location for storing logs (Press enter to use default location): ')

            if path == '' or settings.validate_path(path):
                if not path == '':
                    settings.update_path(path)
                break
            print('Invalid path!')

        # create installation dir
        settings.create_file_loc()

        # install dependencies
        print('\nInstalling dependencies...Please make sure your Python version is >= 3.9.0\n')
        helper.sleep_wait(2)
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

        settings.update_first_launch()
    else:
        print('Current location for Clipboard logs is: ' + settings.get_path())

    print('\nAll set! Keep copying :)')

    # start running in background
    DETACHED_PROCESS = 8
    subprocess.Popen("python helper.py", creationflags=DETACHED_PROCESS, close_fds=True)
