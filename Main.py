from UserView import *
from UserManger import *

def system_run():
    choice = UserView.main_menu()
    if int(choice) == int(1):
        UserManger.log_in()
    else:
        UserManger.sign_up()

def main():

    ali = UserManger()
    ali.log_in()

    while True:
        system_run()

if __name__ == '__main__':
    main()
