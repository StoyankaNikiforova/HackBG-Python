from getpass import getpass
from settings import *


@command_valitation(VALID_COMMANDS_WELCOME)
def welcome_switcher(user_command):
    return WELCOME_SWITCHER[user_command]()


def welcome():
    print(WELCOME_MESSAGE)
    user_command = input(INP_STR)
    welcome_switcher(user_command)


def get_register_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    register(username, password)


@validate_pass()
def register(username, password):
    pass


@command_valitation(VALID_COMMANDS_USER)
def user_switcher(user_command):
    return USER_SWITCHER[user_command]()


def get_login_credentials():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    login(user, password)


@verify_pass()
def login(logged_user, password):
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


@command_valitation(VALID_COMMANDS_EDIT)
def edit_switcher(user_command):
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
