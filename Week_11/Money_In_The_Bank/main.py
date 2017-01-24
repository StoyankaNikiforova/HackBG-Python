import sql_manager
import bank_manager
from settings import HELP_MESSAGE, WELCOME_MESSAGE


def main_menu():
    bank_manager.welcome()



def main():
    main_menu()

if __name__ == '__main__':
    main()
