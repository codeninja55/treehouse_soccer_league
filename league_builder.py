# This Python program will split 18 players from a csv file into 3 separate
# teams. The program will output a txt file that contains the league roster.
# Finally the program will also output 18 separate txt files that will be
# letters to the parents of each player.

import random, csv

def write_teams(teams):
    team_names = ["Dragons", "Raptors", "Sharks"]

    with open('teams.txt', 'w') as file:
        file.write("Soccer League Teams\n\n")
        for team in teams:
            team_name = random.choice(team_names)
            file.write(team_name + "\n")
            team_names.remove(team_name)
            for player in team:
                file.write(', '.join(player) + "\n")

            file.write("\n")


def edit_teams(teams):
    edited_teams = []
    # make a nested list of teams
    for team in teams:
        for player in team:
            # edit the values in the team lists to remove height
            del player['Height (inches)']
            edited_teams.append(list(player.values()))

    print(edited_teams[0])
    # return the teams as a packed tuple
    return edited_teams

def assign_teams():
    # randomly assign players to teams from two separate nested lists
    nonexp_players, exp_players = separate_players()

    teams = [[] for i in range(3)]

    num_nonexp = int(len(nonexp_players) / len(teams))
    num_exp = int(len(exp_players) / len(teams))

    for team in teams:
        # Assign players from list of non-experienced players
        # Remove player from list so player choice cannot be duplicated
        for i in range(num_nonexp):
            choice = random.choice(nonexp_players)
            team.append(choice)
            nonexp_players.remove(choice)

        # Assign players from list of experienced players
        # Remove player from list so player choice cannot be duplicated
        for i in range(num_exp):
            choice = random.choice(exp_players)
            team.append(choice)
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
    edited_teams = edit_teams(teams)
    write_teams(edited_teams)