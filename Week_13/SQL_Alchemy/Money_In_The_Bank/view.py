# import sql_manager
from getpass import getpass
from settings import *
from validators import *
from controler import register, get_user, edit_pass, edit_message


@command_valitation('register', 'login', 'help', 'exit')
def welcome_switcher(user_command, username):
    command = user_command
    WELCOME_SWITCHER = {"register": get_register_credentials, 'login': get_login_credentials, 'helpp': welcome_help, 'exit': exit}
    return WELCOME_SWITCHER[command]()


def welcome():
    print(WELCOME_MESSAGE)
    user_command = input(INP_STR)
    username = 'anonymous'
    return (welcome_switcher(user_command, username))


def get_register_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if username in password:
        raise ValueError("Password can't contain username!")
        password = getpass("Enter your password: ")
    register(username, password)


@command_valitation('info', 'edit', 'help', 'exit')
def user_switcher(user_command, username):
    USER_SWITCHER = {'info': info,
                     'edit': edit,
                     'help': user_help,
                     'exit': exit}
    return USER_SWITCHER[user_command](username)


def get_login_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    login(username, password)


@verify_user()
def create_user(username, password):
    return False


def login(username, password):
    user = get_user(username)
    print(USER_MESSAGE.format(user.username))
    user_command = input(INP_STR)
    user_switcher(user_command, username)


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
def edit_switcher(user_command, username):
    EDIT_SWITCHER = {'message': change_message,
                     'password': change_pass}
    return EDIT_SWITCHER[user_command](username)


def edit(logged_user):
    print(EDIT_MESSAGE)
    user_command = input(INP_STR)
    edit_switcher(user_command, logged_user)


def change_pass(logged_user):
    new_pass = getpass(INP_STR_CHANGE_PASS)
    edit_pass(new_pass, logged_user)


def change_message(logged_user):
    new_message = input(INP_STR_CHANGE_MESSAGE)
    edit_message(new_message, logged_user)


def user_help():
    print(HELP_MESSAGE)
    user_command = input(INP_STR)
    user_switcher(user_command)
