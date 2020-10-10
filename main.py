import subprocess

import values
from helper import create_file_loc

if __name__ == '__main__':
    print('\n*********Welcome to Clipboard log*********\n')

    # install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    print('\nDefault path is C:\\Clipboard-log)')
    print('NOTE: Using ' + values.FILE_PATH + ' as default path for logs.')

    # create default dir
    create_file_loc()

    print('All set! Keep copying :)')

    # start running in background
    DETACHED_PROCESS = 8
    subprocess.Popen("python helper.py", creationflags=DETACHED_PROCESS, close_fds=True)
