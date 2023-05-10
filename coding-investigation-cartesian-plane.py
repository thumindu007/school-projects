import random
import math

def midpoint(player1,player2):
    midpointx,midpointy = (player1['posx']+player2['posx'])/2, (player1['posy']+player2['posy'])/2
    return midpointx, midpointy

def gradient(playercords,destination):
    return round((destination['posy']-playercords['posy']) / (destination['posx']-playercords['posx']), 1)

def distance(point1, point2):
    return round(math.sqrt(((point1['posx'] - point2['posx']) ** 2) + ((point1['posy'] - point2['posy']) ** 2)), 1)

def printinfo(player, otherplayer, destination):
    print("     **PLAYER",player['playertype'],"INFO**     "'\nLocation:',player['posx'],"x",player['posy'],"y\nDistance to Destination:",distance(player, destination),'units\nGradient with destination:',gradient(player, destination),'\nMidpoint with Player',otherplayer['playertype'],':',midpoint(player1, player2),'\n\n')

def destinationlocation(destination):
    print("     **DESTINATION LOCATION**     ",'\nLocation:',destination['posx'],"x",destination['posy'],"y")
#assigns random cords to each player and destination
player1, player2, destination = {'posx':random.randrange(-800, 800, 2), 'posy':random.randrange(-800, 800, 2), 'playertype' : 1}, {'posx':random.randrange(-800, 800, 2), 'posy':random.randrange(-800, 800, 2), 'playertype' : 1}, {'posx':random.randrange(-800, 800, 2), 'posy':random.randrange(-800, 800, 2), 'playertype' : 3}

#prints all the player info
printinfo(player1, player2, destination)
printinfo(player2, player1, destination)
destinationlocation(destination)
print()