import random
import math
from triples import *

# calculates the midpoint between two points given to the function
def calculate_midpoint(player1,player2):
    midpointx,midpointy = (player1['posx']+player2['posx'])/2, (player1['posy']+player2['posy'])/2
    return midpointx, midpointy

def calculate_gradient(playercoords,destination):
    return round((destination['posy']-playercoords['posy']) / (destination['posx']-playercoords['posx']), 1)

def calculate_distance(point1, point2):
    return round(math.sqrt(((point1['posx'] - point2['posx']) ** 2) + ((point1['posy'] - point2['posy']) ** 2)), 1)

def print_info(player, otherplayer, destination):
    print("\n     **PLAYER",player['playertype'],"INFO**     ")
    print('Location:',player['posx'],"x",player['posy'],'y')
    print("Distance to Destination:",calculate_distance(player, destination),'units')
    print('Gradient with destination:',calculate_gradient(player, destination))
    print('Midpoint with Player',otherplayer['playertype'],':',calculate_midpoint(player1, player2),'\n')

def print_destination_info(destination):
    print("\n     **DESTINATION LOCATION**     ",
          '\nLocation:',destination['posx'],"x",destination['posy'],"y\n\n")

def translation_calculator(short, long, direction):
    if direction == 1: return long, short
    elif direction == 2: return short, long
    elif direction == 3: return -short, long
    elif direction == 4: return -long, short
    elif direction == 5: return -long, -short
    elif direction == 6: return -short, -long
    elif direction == 7: return short, -long
    elif direction == 8: return long, -short

def move_player(triples):
    units_to_move = int(input("How much units do you want to move: "))
    direction = int(input("What direction will you like to move"))
    for i in range(len(triples)):
        if triples[i][2] > units_to_move:
            break
        triple_to_move = triples[i]
    short,long = triple_to_move[0], triple_to_move[1]
    return translation_calculator(short, long, direction)
    print("end")

#assigns random cords to each player and destination
class player1class:
    def __init__(self, posx, posy, playertype):
        player1.posx = posx
        player1.posy = posy
        player1.playertype = playertype


player1 = player1class(random.randrange(-800, 800, 1), random.randrange(-800, 800, 1))

player2 = {'posx' : random.randrange(-800, 800, 1), 
            'posy' : random.randrange(-800, 800, 1), 
            'playertype' : 2}
destination = {'posx' : random.randrange(-800, 800, 1), 
               'posy' : random.randrange(-800, 800, 1),
                'playertype' : 3}

#prints all the player info
#print_info(player1, player2, destination)
#print_info(player2, player1, destination)
#print_destination_info(destination)
print(player1)
#while True:
#    print("Player 1, enter your direction and the amount you want to move in it")
#    new_coords = move_player(triples)
#    player1.update({'posx' : player1['posx'] + new_coords[0], 'posy' : player1['posy'] + new_coords[1]})
#    print_info(player1, player2, destination)
#    print("Player 2, enter your direction and the amount you want to move in it")
#    new_coords = move_player(triples)
#    player2.update({'posx' : player2['posx'] + new_coords[0], 'posy' : player2['posy'] + new_coords[1]})
#    print_info(player2, player1, destination)