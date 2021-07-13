import os


def resource_file_initialization():
    resource_dir = "resources-pypass"
    check_dir = os.path.isdir(resource_dir)

    if not check_dir:
        os.makedirs(resource_dir)


def get_password_sources():
    f = open("resources-pypass/pypass-passwords.txt", "r")
    lines_list = f.readlines()
    password_dict = {}
    for x in lines_list:
        source = get_source_from_line(x)
        encrypted_password = get_encrypted_password_from_line(x)
        password_dict[source] = encrypted_password
    f.close()
    return password_dict

def get_source_from_line(line):
    end_index = line.index(':')
    source = line[0:end_index]
    return source


def get_encrypted_password_from_line(line):
    start_index = line.index('{') + 1
    end_index = line.index('}')
    encrypted_password = line[start_index:end_index]
    return encrypted_password

def print_list_of_sources(password_dict):
    keys_list = password_dict.keys()
    for x in keys_list:
        print(x + "\n")