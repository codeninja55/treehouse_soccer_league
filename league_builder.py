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

    # TODO Remove the print statements
    print(nonexp_players[0])
    print(exp_players[0])

    # return the two list of players to be separated in another function
    return nonexp_players, exp_players

def assign_teams(nonexp_players, exp_players):
    # randomly assign players to teams from two separate lists

    nonexp_players, exp_players = separate_players()

    sharks = []
    dragons = []
    raptors = []


if __name__ == "__main__":
    separate_players()