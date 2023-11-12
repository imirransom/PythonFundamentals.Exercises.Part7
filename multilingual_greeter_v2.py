class ModeChange:
    def __int__(self):
        pass


    def user_choice(self, choice):
        choice = input("What you mode would you like?:")
        print("1. Admin\n2. User")
        choice = choice.lower()
        return choice

    def mode_choice(self, selection):
        while selection == "1" or selection == "admin":
            admin_choice = input("You have chosen admin mode, what would you like to do?")
            admin_choice = admin_choice.lower()
            print("1. Support for additional languages\n2. Update existing languages")
            if admin_choice == "1" or "support for additional languages":
                print('please add support')
                break
            elif admin_choice == "2" or admin_choice == "update existing languages":
                print("Please update the existing languages")
                break
            else:
                print("Wrong selection, please try again")