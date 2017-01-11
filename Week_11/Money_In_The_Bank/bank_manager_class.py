class bankManager():
    def register():
        pass

    def login(logged_user):
        username = logged_user.get_username
        print(USER_MESSAGE.format(username))
        user_command = input(INP_STR)
        return USER_SWITCHER[user_command]()

    def welcome_help():
        print(WELCOME_MESSAGE)

    def exit():
        exit()

    def info(logged_user):
        username = logged_user.get_username
        balance = logged_user.get_balance
        message = logged_user.get_message
        print(INFO_MESSAGE.format(username, balance, message))

    def edit(logged_user):
        print(EDIT_MESSAGE)
        user_command = input(INP_STR)
        return EDIT_SWITCHER[user_command]()

    def change_pass(logged_user):
        new_pass = input(INP_STR_CHANGE_PASS)
        sql_manager.change_pass(new_pass, logged_user)

    def change_message(logged_user):
        new_message = input(INP_STR_CHANGE_MESSAGE)
        sql_manager.change_message(new_message, logged_user)

    def user_help():
        print(HELP_MESSAGE)
        user_command = input(INP_STR)
        return USER_SWITCHER[user_command]()
