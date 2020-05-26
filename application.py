import data


print(f'''\n\n\t
        |------------------------------------|
        |-----Basketball Team Stat Tool------|
        |------------------------------------|''')


def start_application():
    '''Start of the application'''
    while True:
        try:
            option_1 = int(input(f'''\t
        |------------------------------------|
        |----------------Menu----------------|
        |------------------------------------|
        |-------Here are your choices:-------|
        |-------1. Display Team Stats--------|
        |-------2. Quit----------------------|
        |----------------------------------> '''))
            if option_1 > 2 or option_1 < 1:
                print(f'''\t
        |---------Not a valid number.--------|
        |-------------Try again.-------------|
        |------------------------------------|''')
            elif option_1 == 1:
                return data.team_menu()
            elif option_1 == 2:
                print(f'''\t
        |------------------------------------|
        |-------------Thank you!-------------|
        |------------------------------------|''')
                break
        except ValueError or NameError:
            print(f'''\t
        |---------Not a valid option.--------|
        |-------------Try again.-------------|''')
            continue

if __name__ == '__main__':
    start_application()
