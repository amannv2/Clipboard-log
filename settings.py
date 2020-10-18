import json
import os

FILE_NAME = 'settings.json'
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


def get_settings_data():
    with open(FILE_NAME) as settings:
        data = json.load(settings)
    return data


def set_settings_data(new_data):
    with open(FILE_NAME, 'w') as settings:
        json.dump(new_data, settings)


def update_path(new_path):
    data = get_settings_data()
    data['FILE_PATH'] = new_path
    set_settings_data(data)


def reset_path():
    data = get_settings_data()
    data['FILE_PATH'] = data['DEFAULT_PATH']
    set_settings_data(data)


def get_path():
    data = get_settings_data()
    return data['FILE_PATH']


def get_default_path():
    data = get_settings_data()
    return data['DEFAULT_PATH']


def first_launch():
    data = get_settings_data()
    return data['FIRST']


def update_first_launch():
    data = get_settings_data()
    data['FIRST'] = False
    set_settings_data(data)


def add_to_startup():
    data = get_settings_data()
    data['STARTUP'] = True
    set_settings_data(data)


def remoe_from_startup():
    data = get_settings_data()
    data['STARTUP'] = False
    set_settings_data(data)
