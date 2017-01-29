DB_NAME = 'sqlite:///BANK.db'

INP_STR = '$$$>'
INP_STR_CHANGE_PASS = 'Enter your new password: '
INP_STR_CHANGE_MESSAGE = 'Enter your new message: '

HELP_MESSAGE = '''[info]- for showing account info,
                  [edit] - for changing passowrd or message'''

WELCOME_MESSAGE = '''Welcome to our bank service!!!
                    Please enter:
                    [register]- for registrate in our system,
                    [login] - for login,
                    [help] - for help,
                    [exit] - for exit'''

VALID_COMMANDS_WELCOME = ['register', 'login', 'help', 'exit']


USER_MESSAGE = '''Welcome {}!!!
                    Please enter:
                    [info]- to view your profile,
                    [edit] - to edit your profile,
                    [help] - for help'''

VALID_COMMANDS_USER = ['info', 'edit', 'help', 'exit']

INFO_MESSAGE = '''Welcome you are logged in as: {},
Your ID is: {},
Your BALANCE is: {},
Your MESSAGE is: {} '''


EDIT_MESSAGE = '''You want to change your:
                [message] or [password]
                Please enter keyword: '''

VALID_COMMANDS_EDIT = ['message', 'password']

NOT_VALID_MESSAGE = 'Not a valid command'

WRONG_VALUE = '''The password must have More then 8 symbols,
                    capital letters, and numbers,
                    and a special symbol'''

PASS_REG = '[\d{1,}(\W{1,})(\D)]{8,}'
