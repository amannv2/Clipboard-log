import json
import os

PATH_NOT_ALLOWED = {'C:', 'C:\\', 'C:\\\\', 'C:/', 'C://'}


def validate_path(file_path):
    if file_path in PATH_NOT_ALLOWED:
        print('Permission denied! Please choose another location.')
        return False
    if os.path.isdir(file_path):
        return True
    return False


def create_file_loc():
    path = get_path()
    if not validate_path(path):
        os.makedirs(path, 777)


def update_path(new_path):
    with open('settings.json') as settings:
        data = json.load(settings)
    data['FILE_PATH'] = new_path

    with open('settings.json', 'w') as settings:
        json.dump(data, settings)


def reset_path():
    with open('settings.json') as settings:
        data = json.load(settings)
    data['FILE_PATH'] = data['DEFAULT_PATH']

    with open('settings.json', 'w') as settings:
        json.dump(data, settings)


def get_path():
    with open('settings.json') as settings:
        data = json.load(settings)
    return data['FILE_PATH']


def get_default_path():
    with open('settings.json') as settings:
        data = json.load(settings)
    return data['DEFAULT_PATH']


def first_launch():
    with open('settings.json') as settings:
        data = json.load(settings)
    return data['FIRST']


def update_first_launch():
    with open('settings.json') as settings:
        data = json.load(settings)
    data['FIRST'] = False
    with open('settings.json', 'w') as settings:
        json.dump(data, settings)
