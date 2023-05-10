import random
import math
from triples import *

# calculates the midpoint between two points given to the function
def calculate_midpoint(player1,player2):
    midpointx,midpointy = (player1['posx']+player2['posx'])/2, (player1['posy']+player2['posy'])/2
    return midpointx, midpointy

def calculate_gradient(playercords,destination):
    return round((destination['posy']-playercords['posy']) / (destination['posx']-playercords['posx']), 1)

def calculate_distance(point1, point2):
    return round(math.sqrt(((point1['posx'] - point2['posx']) ** 2) + ((point1['posy'] - point2['posy']) ** 2)), 1)

def print_info(player, otherplayer, destination):
    print("     **PLAYER",player['playertype'],"INFO**     "
          '\nLocation:',player['posx'],"x",player['posy'],
          "y\nDistance to Destination:",calculate_distance(player, destination),
          'units\nGradient with destination:',calculate_gradient(player, destination),
          '\nMidpoint with Player',otherplayer['playertype'],
          ':',calculate_gradient(player1, player2),'\n\n')

def print_destination_info(destination):
    print("     **DESTINATION LOCATION**     ",
          '\nLocation:',destination['posx'],"x",destination['posy'],"y")

def move_player(player):
    units_to_move = int(input("How much units do you want to move: "))
    direction = int(input("What direction will you like to move"))
    for i in range(units_to_move,0,-1):
        print(i)
        for x in range(len):
            
        if i == triples[0][2]:
            break
    print("end")
    
#assigns random cords to each player and destination
player1 = {'posx':random.randrange(-800, 800, 1), 
            'posy':random.randrange(-800, 800, 1), 
            'playertype' : 1}
player2 = {'posx':random.randrange(-800, 800, 1), 
            'posy':random.randrange(-800, 800, 1), 
            'playertype' : 2}
destination = {'posx':random.randrange(-800, 800, 1), 
               'posy':random.randrange(-800, 800, 1),
                'playertype' : 3}
#prints all the player info
print_info(player1, player2, destination)
print_info(player2, player1, destination)
print_destination_info(destination)
move_player(player1)
print()