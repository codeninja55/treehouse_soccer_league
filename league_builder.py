# This Python program will split 18 players from a csv file into 3 separate
# teams. The program will output a txt file that contains the league roster.
# Finally the program will also output 18 separate txt files that will be
# letters to the parents of each player.

import random, csv

def write_letters(teams):
    # iterate over list and for ea team and player, write a new txt file as letter
    for i in range(len(teams)):
        team_name = teams[i]['team']
        tr_date = teams[i]['tr_date']
        tr_time = teams[i]['tr_time']

        for player in teams[i]['players']:
            # use the players name as the file name with lowercase
            file_name = player['Name'].lower().replace(" ","_") + ".txt"
            with open(file_name, 'w') as letter:
                # each file begins with text "Dear" followed by guardians names
                letter.write('Dear {},\n\n'.format(player['Guardian Name(s)']))
                # include additional information, player's name, team's name,
                # and date and time of first practice
                letter_content ="""
Your child {child}, has beed added to the following team ({team})
for the upcoming League season.

Your child's first training session details are as follows:
Date: {tr_date}
Time: {tr_time}

Thank you for your support and we look forward to an enjoyable and fun
upcoming season with {child}.
                """.format(child=player['Name'],
                           team=team_name.capitalize(),
                           tr_date=tr_date,
                           tr_time=tr_time)

                letter.write(letter_content)


def write_teams(teams):
    edited_teams = [[] for i in range(len(teams))]

    for i in range(len(teams)):
        edited_teams[i].append(teams[i]['team'])
        for player in teams[i]['players']:
            # edit the values in the team lists to remove height
            try:
                del player['Height (inches)']
            except KeyError:
                pass
            # append a list of the values so as to use join method to write
            edited_teams[i].append(list(player.values()))

    with open('teams.txt', 'w') as file:
        file.write("Soccer League Teams\n\n")
        for team in edited_teams:
            file.write(team[0].capitalize() + '\n')

            for player in team[1:]:
                file.write(', '.join(player) + "\n")

            file.write("\n")


def assign_teams():
    # randomly assign players to teams from two separate nested lists
    nonexp_players, exp_players = separate_players()

    # create each team as a dict with keys including team practice
    dragons = dict(team='dragons', players=list(), tr_date='03/04/2017',
                   tr_time='17:00')
    raptors = dict(team='raptors', players=list(), tr_date='04/04/2017',
                   tr_time='17:30')
    sharks = dict(team='sharks', players=list(), tr_date='05/04/2017',
                  tr_time='18:00')

    teams = [dragons, raptors, sharks]

    num_nonexp = int(len(nonexp_players) / len(teams))
    num_exp = int(len(exp_players) / len(teams))

    for t in range(len(teams)):
        # Assign players from list of non-experienced players
        # Remove player from list so player choice cannot be duplicated
        for p in range(num_nonexp):
            choice = random.choice(nonexp_players)
            teams[t]['players'].append(choice)
            nonexp_players.remove(choice)

        # Assign players from list of experienced players
        # Remove player from list so player choice cannot be duplicated
        for p in range(num_exp):
            choice = random.choice(exp_players)
            teams[t]['players'].append(choice)
            exp_players.remove(choice)

    # return a list of teams
    return teams


def separate_players():
    # create separate list of players with and without experience

    exp_players = []
    nonexp_players = []

    # import csv file and create list of players
    with open('soccer_players.csv', 'r') as file:
        players = csv.DictReader(file, delimiter=',')

        for row in players:
            if row['Soccer Experience'].upper() == 'YES':
                exp_players.append(row)
            else:
                nonexp_players.append(row)

    # return the two nested list of players to be separated in another function
    return nonexp_players, exp_players


if __name__ == "__main__":
    separate_players()
    teams = assign_teams()
    write_teams(teams)
    write_letters(teams)