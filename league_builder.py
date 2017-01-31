# This Python program will split 18 players from a csv file into 3 separate
# teams. The program will output a txt file that contains the league roster.
# Finally the program will also output 18 separate txt files that will be
# letters to the parents of each player.

import random, csv

def separate_players():
    # create separate list of players with and without experience

    exp_players = []
    nonexp_players = []

    # import csv file
    # create list of players
    # return the list
    with open('soccer_players.csv', 'r') as file:
        players = csv.DictReader(file, delimiter=',')

        for player in players:
            if player['Soccer Experience'].upper() == 'YES':
                exp_players.append(player)
            else:
                nonexp_players.append(player)

    # return the two list of players to be separated in another function
    return nonexp_players, exp_players

def assign_teams():
    # randomly assign players to teams from two separate lists

    nonexp_players, exp_players = separate_players()

    dragons = []
    raptors = []
    sharks = []
    teams = [dragons, raptors, sharks]

    num_nonexp = int(len(nonexp_players) / len(teams))
    num_exp = int(len(exp_players) / len(teams))

    for team in teams:
        # Assign players from list of non-experienced players
        # Remove player from list so player choice cannot be duplicated
        for i in range(num_exp):
            choice = random.choice(nonexp_players)
            team.append(choice)
            nonexp_players.remove(choice)

        # Assign players from list of non-experienced players
        # Remove player from list so player choice cannot be duplicated
        for i in range(num_exp):
            choice = random.choice(exp_players)
            team.append(choice)
            exp_players.remove(choice)

    return dragons, raptors, sharks

if __name__ == "__main__":
    separate_players()
    assign_teams()