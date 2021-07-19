import os

import utils.encryptor as encrypt
import utils.tools as util
import pyperclip as pc


def greetings():
    on = True
    while on:
        util.resource_file_initialization()
        print("PyPass - press 3 to exit")
        input_result = input('What do you wish to do? Press 1 to add a new password, press 2 to retrieve a password. '
                             '-> ')
        if input_result == "1":
            add_new_password()
        elif input_result == "2":
            retrieve_password()
        elif input_result == "3":
            on = False
        else:
            print("invalid input")


def add_new_password():
    passkey = input("Enter your passkey -> ")
    password_raw = input("Enter password to encrypt -> ")
    password_for = input("What is this password for? -> ")

    key = encrypt.hash_password(passkey)
    encrypted_password = encrypt.encrypt_password(password_raw, key)
    output_string = password_for + ': {' + encrypted_password.decode() + '}\n'
    f = open('resources-pypass/pypass-passwords.txt', 'a+')
    f.write(output_string)
    f.close()


def retrieve_password():
    source_password_dict = util.get_password_sources()
    passkey = input("Enter your passkey -> ")
    passkey = encrypt.hash_password(passkey)
    print("Which password do you want to retrieve?\n")
    util.print_list_of_sources(source_password_dict)
    source = input("--> ")
    if source_password_dict.keys().__contains__(source):
        source = source_password_dict.get(source)
        decrypted_password = encrypt.decrypt_password(source, passkey)
        # clipboard.copy(decrypted_password)
        pc.copy(decrypted_password)
        print("*copied to clipboard*")
