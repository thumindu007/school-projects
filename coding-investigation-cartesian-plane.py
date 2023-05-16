import random
import time
from pytimedinput import timedInput
import math
from triples import * #imports the triples list

#creates a class for the template of the players
class Player:
    def __init__(self, posx, posy, playertype):
        self.posx = posx
        self.posy = posy
        self.playertype = playertype
        self.spacebuffer = 10

    def print_info(self, destination, otherplayer):
        print("\n     **PLAYER",self.playertype,"INFO**     ")
        print('Location:',self.posx,"x",self.posy,'y')
        print("Distance to Destination:",calculate_distance(self, destination),'units')
        print('Gradient with destination:',calculate_gradient(self, destination))
        print('Midpoint with other Player:',calculate_midpoint(self, otherplayer),'\n')

    def check_win(self, otherplayer, destination):
        dis_otherplayer = calculate_distance(self, otherplayer)
        dis_destination = calculate_distance(self, destination)
        if dis_otherplayer < self.spacebuffer or dis_destination < self.spacebuffer:
            return True
        else:
            return False

# calculates the midpoint between two points given to the function
def calculate_midpoint(player1,player2):
    midpointx,midpointy = (player1.posx + player2.posx) / 2, (player1.posy + player2.posy)/2
    return midpointx, midpointy

#calculates the gradient between any 2 points
def calculate_gradient(playercoords,destination):
    return round((destination.posy - playercoords.posy) / (destination.posx - playercoords.posx), 1)

#calculates the listance between any 2 points
def calculate_distance(point1, point2):
    return round(math.sqrt(((point1.posx - point2.posx) ** 2) + ((point1.posy - point2.posy) ** 2)), 1)

#prints the infomation about the destination
def print_destination_info(destination):
    print("\n     **DESTINATION LOCATION**     ",
          '\nLocation:',destination.posx,"x",destination.posy,"y\n\n")

#calculates the 2 numbers that will be added to the coordinates of a player to make them move in a certain direction
def translation_calculator(short_side, long_side, direction): #short side is the first number of the triple and long side is the second
    index = direction - 1
    direction_multiplier = directions[index]
    short_side = short_side * direction_multiplier[1]
    long_side = long_side * direction_multiplier[2]
    if direction_multiplier[3] is True:
        short_side, long_side = long_side, short_side
    print(short_side, long_side)
    return short_side, long_side

def move_player(possible_moves):
    units_to_move_direction, timedout = timedInput("What is your move?: ", timeout=10)
    if timedout:
        print("Timed out when waiting for input.")
        units_to_move_direction = [random.randrange(5, 800, 1), random.randrange(1, 8, 1)]
        time.sleep(3)
    else:
        units_to_move_direction = units_to_move_direction.split()
    units_to_move, direction = int(units_to_move_direction[0]), int(units_to_move_direction[1])
    for move in possible_moves:
        if move[2] > units_to_move:
            break
        triple_to_move = move
    short,long = triple_to_move[0], triple_to_move[1]
    return translation_calculator(short, long, direction)

#creates a list of the possible directions a player can move
directions = [[1, 1, 1, True],
              [2, 1, 1, False],
              [3, -1, 1, False],
              [4, 1, -1, True],
              [5, -1, -1, True],
              [6, -1, -1, False],
              [7, 1, -1, False],
              [8, 1, -1, True]]

#uses the class as a template to create players with random coordinates
player1 = Player(random.randrange(-800, 800, 1), random.randrange(-800, 800, 1), 1)
player2 = Player(random.randrange(-800, 800, 1), random.randrange(-800, 800, 1), 2)
target_destination = Player(random.randrange(-800, 800, 1), random.randrange(-800, 800, 1), 3)

#declaires that no one has won the game yet
PLAYER1WIN = False
PLAYER2WIN = False

#prints all the player info
player1.print_info(target_destination, player2)
player2.print_info(target_destination, player1)
print_destination_info(target_destination)

while PLAYER1WIN is False and PLAYER2WIN is False:
    print("Player 1, enter your direction and the amount you want to move in it")
    new_coords = move_player(triples)
    player1.posx, player1.posy = player1.posx + new_coords[0], player1.posy + new_coords[1]
    player1.print_info(target_destination, player2)
    if player1.check_win(player2, target_destination):
        WINNER = 'Player 1'
        PLAYER1WIN = True
    print_destination_info(target_destination)
    
    print("Player 2, enter your direction and the amount you want to move in it")
    new_coords = move_player(triples)
    player2.posx, player2.posy = player2.posx + new_coords[0], player2.posy + new_coords[1]
    player2.print_info(target_destination, player2)
    if player2.check_win(player1, target_destination):
        WINNER = 'Player 2'
        PLAYER1WIN = True
    print_destination_info(target_destination)

print(WINNER,"has won the game!")
