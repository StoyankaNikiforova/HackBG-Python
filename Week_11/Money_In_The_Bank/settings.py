DB_NAME = 'BANK.db'

INP_STR = '$$$> '
INP_STR_CHANGE_PASS = 'Enter your new password: '
INP_STR_CHANGE_MESSAGE = 'Enter your new message: '

HELP_MESSAGE = '''[info]- for showing account info,
                  [edit] - for changing passowrd or message'''

HELP_USER_SWITCHER = {'info': info, 'edit': edit}

WELCOME_MESSAGE = '''Welcome to our bank service!!!
                    Please enter:
                    [register]- for registrate in our system,
                    [login] - for login,
                    [help] - for help,
                    [exit] - for exit'''

VALID_COMMANDS_WELCOME = ['register', 'login', 'help', 'exit']

WELCOME_SWITCHER = {'register': get_register_credentials, 'login': get_login_credentials, 'help': welcome_help, 'exit': exit}

USER_MESSAGE = '''Welcome {}!!!
                    Please enter:
                    [info]- to view your profile,
                    [edit] - to edit your profile,
                    [help] - for help'''

VALID_COMMANDS_USER = ['info', 'edit', 'help', 'exit']
USER_SWITCHER = {'info': info, 'edit': edit, 'help': user_help, 'exit': exit}

INFO_MESSAGE = '''Welcome you are logged in as: {},
Your ID is: {},
Your BALANCE is: {},
Your MESSAGE is: {} '''


EDIT_MESSAGE = '''You  to change your:
                [message] or [password]
                Please enter keyword: '''

VALID_COMMANDS_EDIT = ['message', 'password']
EDIT_SWITCHER = {'message': change_message, 'password': change_pass}

NOT_VALID_MESSAGE = 'Not a valid command'
