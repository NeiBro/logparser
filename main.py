from log_search import search
from statistic import statistic

def display_menu():
    print('What you want to do with log?')
    print('1. Search via parameter')
    print('2. Get statistic')

def get_answer():
    while True:
        try:
            main_answer = int(input())
            if 1 <= main_answer <= 2:
                return main_answer
            else:
                print('Please enter number between 1 and 2.')
        except ValueError:
            print('Please enter valid number.')

def main():
    display_menu()
    main_answer = get_answer()
    if main_answer == 1:
        search()
    if main_answer == 2:
        statistic()

if __name__ == '__main__':
    main()