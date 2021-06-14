# from constants import teams/players
# from copy import deepcopy
from constants import TEAMS
from constants import PLAYERS
from copy import deepcopy

# begin function to 'clean' players
def clean_players(lst):
    # create deepcopy of players
    players_copy = deepcopy(lst)

    # loop through players
    for player in players_copy:
        # if player[exp] = 'YES ... change value to True
        if player['experience'] == 'YES':
            player['experience'] = True
        # else ... change to False
        else:
            player['experience'] = False

        # player[guardians] split using ' and '
        player['guardians'] = player['guardians'].split(' and ')

        # player[height] strip ' inches' and wrap in int()
        player['height'] = int(player['height'].strip(' inches'))
    
    #return deepcopied_players
    return players_copy

# begin balance_teams function 
def balance_teams(lst, plyrs):
    # Create new dict for returning teams balanced.
    new_teams = {}

    # Create key and value for each team in TEAMS
    for team in lst:
        new_teams[team] = []

    #Create temporary lists for experienced and inexperienced players
    experienced_players = []
    inexperienced_players = []

    # Copy players from players list to either experienced or inexperienced
    for player in plyrs:
        temp_player = player.copy()
        if player['experience'] == True:
            experienced_players.append(temp_player)
        else: 
            inexperienced_players.append(temp_player)
    
    team_names = []
    for team in new_teams:
        team_names.append(team)

    for num in range(-1, len(experienced_players) - 1):
        team = team_names[num % len(new_teams)]
        new_teams[team].append(experienced_players[num])
    
    for num in range(len(inexperienced_players)):
        team = team_names[num % len(team_names)]
        new_teams[team].append(inexperienced_players[num])

    #return dict
    return new_teams

# write stats tool function
def stats_tool(dict):
    print('\n\n BASKETBALL TEAM STATS TOOL')
    
    #begin program loop
    while True:
        
        # Display menu options
        print('\n' + ('-' * 5) + ' MENU ' + ('-' * 5))
        print('\n Here are your choices:')
        print('    A) Display Team Stats')
        print('    B) Quit')

        # Start checking for Exceptions
        try:

            # User input one
            user_choice_one = input('\nPlease enter an option: \n>')
                
            # If user input, go to next option
            if user_choice_one.upper() == 'A':
                
                # Begin new loop for second part
                while True:
                    try:
                        # Empty team names list
                        team_names = []

                        # print numbered options for available teams using enumerate
                        # also need ordered list of names, so ammend each team_name to team_names list
                        for count, team in enumerate(dict):
                            print(f'{count + 1}) {team}')
                            team_names.append(team)

                        # User Input two
                        user_choice_two = int(input('\nPlease enter an option: \n>'))

                        # Check user input is within correct range
                        if user_choice_two not in range(1, len(team_names) + 1):
                            raise IndexError('Please enter a number between 1 and {}'.format(len(team_names)))
                                        
                        # Set variables for all team info:
                        team_choice = team_names[user_choice_two - 1]
                        total_players = len(dict[team_choice])
                        
                        # Empty variables / lists for calculations:
                        team_players = []
                        guardians = []
                        inex_players = 0
                        expd_players = 0
                        total_height = 0

                        # For loop outputs info to variables above.
                        for players in dict[team_choice]:
                            team_players.append(players['name'])

                            for guardian in players['guardians']:
                                guardians.append(guardian)

                            if players['experience'] == True:
                                expd_players += 1
                            else:
                                inex_players += 1

                            total_height += players['height']
                        
                        # Calculate average height
                        average_height = total_height / len(team_players)

                        # Now prints all information
                        print(f'\nTeam: {team_choice} Stats')
                        print('-' * 20)

                        print(f'Total Players: {total_players}')
                        print(f'Experienced Players: {expd_players}.')
                        print(f'Inexperienced Players: {inex_players}.')
                        print(f'Average height of team: {average_height}')

                        print('\nPlayers on team:')
                        print(*team_players, sep=", ")

                        print('\nGuardians:')
                        print(*guardians, sep=", ")
                        
                        # Option to continue
                        user_cont = input('\nPress ENTER to return to menu...')

                        # Pressing ENTER will break the loop and return to the menu, either way.
                        if user_cont == '':
                            break
                        continue

                    # Outputs exception message for IndexError        
                    except IndexError as err:
                        print(f'There was an error. {err}.')
            
            # Exits the program (breaking the loop)
            elif user_choice_one.upper() == 'B':
                print('Thanks for using the Basketball Stats Tool.')
                break
            
            # Any other entry other will raise ValueError
            else: 
                raise ValueError('Please enter \'A\' or \'B\'.')

        # Outputs ValueError Message if user input is incorrect.
        except ValueError as err:
            print(f'There was an error. {err}')
    

    
# write dunder main
if __name__ == "__main__":
    # call functions inside dunder main
    new_players = clean_players(PLAYERS)
    balanced_teams = balance_teams(TEAMS, new_players)

    stats_tool(balanced_teams)
