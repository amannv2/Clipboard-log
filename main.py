import subprocess

from helper import create_file_loc, validate_path, sleep_wait, all_values, main

if __name__ == '__main__':

    print('\n*********Welcome to Clipboard log*********\n')

    # create default dir
    create_file_loc()

    print('Default location is C:\\Clipboard-log')
    while True:
        path = input('\nPlease enter a location for storing logs (Press enter to use default location): ')

        if path == '' or validate_path(path):
            if not path == '':
                all_values.update_filepath(path)
            break
        print('Invalid path!')

    # install dependencies
    print('\nInstalling dependencies...Please make sure your Python version is >= 3.9.0\n')
    sleep_wait(2)
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    print('\nAll set! Keep copying :)')

    main()
    # start running in background
    # DETACHED_PROCESS = 8
    # subprocess.Popen("python helper.py", creationflags=DETACHED_PROCESS, close_fds=True)
