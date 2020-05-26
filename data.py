import constants
import copy
import random


players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
# Deep copy made because PLAYERS and TEAMS cannot change.


experienced = []
not_experienced = []


def clean_data():
    '''Cleans data by changing height to an integer.
       Changes experience to a boolean value (True or False).
       Split guardians into list.'''
    for player_stats in players:
        if player_stats['experience'] == 'YES':
            player_stats['experience'] = True
        else:
            player_stats['experience'] = False
        player_stats['guardians'] = player_stats['guardians'].split('and')
        player_stats['height'] = int(player_stats['height'][:2])
    for player in players:
        if player['experience'] is True:
            experienced.append(player)
        else:
            not_experienced.append(player)

clean_data()

team_panthers = []
team_bandits = []
team_warriors = []
exp_players = int(len(experienced) / len(teams))
not_exp_players = int(len(not_experienced) / len(teams))


def balance_teams(team):
    while len(experienced) != 0 and len(team) < 3:
        team.append(experienced.pop(random.randrange(len(experienced))))
    while len(not_experienced) != 0 and len(team) < 6:
        team.append(not_experienced.pop(random.randrange(len(not_experienced))))


def dict_teams(team):
    '''Turns individual teams into dictionaries with a numeric index.'''
    index = 1
    team_dict = {}
    for player in team:
        team_dict[index] = player
        index += 1
    return team_dict


def print_boxed(string):
    length = len(string)
    needed_length = len('|------------------------------------|') - 5
    diff = needed_length - length
    dash = '-' * diff
    output = f'\t|--' + string + ' ' + dash + '|'
    print(output)


def team_height(team):
    '''Shows average player height for each team.'''
    total = 0
    for key, value in team.items():
        total += value['height']
    team_avg_height = total / len(team)
    return team_avg_height


def guardians_list():
    '''Creates a comma seperated list of player guardians.'''
    first_guardians = []
    first_players = []
    for player in players:
        player_name = [player['name']]
        first_players = first_players + player_name
        if len(player['guardians']) == 1:
            guardians = [player['guardians'][0]]
            first_guardians = first_guardians + guardians
        if len(player['guardians']) > 1:
            guardian_one = [player['guardians'][0]]
            guardians_two = [player['guardians'][1]]
            first_guardians = first_guardians + guardian_one + guardians_two
    print(f'\nThe Player Guardians.\n')
    print(', '.join(first_guardians))
    print(f'\nThe Player Names.\n')
    print(', '.join(first_players))
    print('')


def team_stats(team):
    '''Shows team stats and allows for input.'''
    num = len('------------------------------------')
    print_boxed(f'Total Players: {len(team)}')
    print_boxed(f'Experienced Players: {int(len(team)/2)}')
    print_boxed(f'Inexperienced players: {int(len(team)/2)}')
    print_boxed(f'Average Player Height: {round(team_height(team))} inches')
    print(f'''
        |------------------------------------|
        |------------Player List-------------|
        |------------------------------------|''')
    for key, value in team.items():
        sub = len(value['name'])
        differnece = num - sub
        diff = (' ' + ('-' * (differnece - 6)))
        print(f"\t|-{key}. {value['name']}{diff}|")
    print(f'''
        |------------------------------------|
        |----------Player Guardians----------|
        |------------------------------------|''')
    for key, value in team.items():
        sub = len(value['guardians'])
        differnece = num - sub
        diff = (' ' + ('-' * (differnece - 30)))
        print(f"\t|-{key}. {value['guardians']}{diff}|")
    while True:
        try:
            option_3 = int(input(f'''\t
        |------------------------------------|
        |--------------Options---------------|
        |------------------------------------|
        |-----7. View list of guardians------|
        |-----8. Return to team selection----|
        |-----9. Exit program----------------|
        |----------------------------------> '''))
            if option_3 == 7:
                return guardians_list()
                print(f'''/t
        |------------------------------------|
        |----------Player Guardians----------|
        |------------------------------------|''')
            elif option_3 == 8:
                team_menu()
            elif option_3 < 7 or option_3 > 10:
                print(f'''\t
        |---------Not a valid number.--------|
        |-------------Try again.-------------|
        |------------------------------------|''')
            elif option_3 == 9:
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


def team_menu():
    balance_teams(team_panthers), balance_teams(team_bandits)
    balance_teams(team_warriors)
    panthers = dict_teams(team_panthers)
    bandits = dict_teams(team_bandits)
    warriors = dict_teams(team_warriors)
    while True:
        try:
            option_2 = int(input(f'''\t
        |------------------------------------|
        |-------Enter an option > 1----------|
        |-------1. Panthers------------------|
        |-------2. Bandits-------------------|
        |-------3. Warriors------------------|
        |------------------------------------|
        |----------------------------------> '''))
            if option_2 == 1:
                print(f'''\t
        |------------------------------------|
        |--------------Panthers--------------|
        |------------------------------------|''')
                team_stats(panthers)
            elif option_2 == 2:
                print(f'''\t
        |------------------------------------|
        |--------------Bandits---------------|
        |------------------------------------|''')
                team_stats(bandits)
            elif option_2 == 3:
                print(f'''\t
        |------------------------------------|
        |--------------Warriors--------------|
        |------------------------------------|''')
                team_stats(warriors)
            elif option_2 > 3 or option_2 < 1:
                print(f'''\t
        |---------Not a valid number.--------|
        |-------------Try again.-------------|
        |------------------------------------|''')
        except ValueError or NameError:
            print(f'''\t
        |---------Not a valid option.--------|
        |-------------Try again.-------------|''')