import sql_manager
from getpass import getpass
from settings import *
from validators import *


@command_valitation('register', 'login', 'help', 'exit')
def welcome_switcher(user_command):
    command = user_command
    WELCOME_SWITCHER = {"register": get_register_credentials, 'login': get_login_credentials, 'helpp': welcome_help, 'exit': exit}
    return WELCOME_SWITCHER[command]()


def welcome():
    print(WELCOME_MESSAGE)
    user_command = input(INP_STR)
    return (welcome_switcher(user_command))


def get_register_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if username in password:
        raise ValueError("Password can't contain username!")
        password = getpass("Enter your password: ")
    sql_manager.register(username, password)


@command_valitation('info', 'edit', 'help', 'exit')
def user_switcher(user_command):
    USER_SWITCHER = {'info': info,
                     'edit': edit,
                     'help': user_help,
                     'exit': exit}
    return USER_SWITCHER[user_command]()


def get_login_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    login(user, password)


@verify_pass()
def login(username, password):
    user = sql_manager.get_user(username, password)
    username = logged_user.get_username
    print(USER_MESSAGE.format(username))
    user_command = input(INP_STR)
    user_switcher(user_command)


def welcome_help():
    welcome()


def exit():
    exit()


def info(logged_user):
    username = logged_user.get_username
    balance = logged_user.get_balance
    message = logged_user.get_message
    print(INFO_MESSAGE.format(username, balance, message))


@command_valitation('message', 'password')
def edit_switcher(user_command):
    EDIT_SWITCHER = {'message': change_message,
                     'password': change_pass}
    return EDIT_SWITCHER[user_command]()


def edit(logged_user):
    print(EDIT_MESSAGE)
    user_command = input(INP_STR)
    edit_switcher(user_command)


def change_pass(logged_user):
    new_pass = input(INP_STR_CHANGE_PASS)
    sql_manager.change_pass(new_pass, logged_user)


def change_message(logged_user):
    new_message = input(INP_STR_CHANGE_MESSAGE)
    sql_manager.change_message(new_message, logged_user)


def user_help():
    print(HELP_MESSAGE)
    user_command = input(INP_STR)
    user_switcher(user_command)
