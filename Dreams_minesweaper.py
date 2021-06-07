#
#
#   Dreams MineSweeper
#
#

import random
from graphics import *
import time

class node():
    val = 0
    
    def __init__(self, val):
        self.val = val

def print_matrix(my_matrix):
    for i in range(0,MAX_I):
        for j in range(0,MAX_J):
            item = my_matrix[i][j]
            print( item.val, ' ', end='')
        print()

def set_xy(my_matrix, x, y):
    my_matrix[x][y].val = 3

    i= max(x-3, 0)

    while i < x+3 and i<MAX_I:
        j= max(y-3, 0)
        while j < y+3 and j<MAX_J:
            my_matrix[i][j].val = max(my_matrix[i][j].val, 3 - max(max(j-y,y-j),max(i-x,x-i)))           
            j+=1
        i+=1


def init_objects(guess_matrix):
    for i in range(0,MAX_I):
        for j in range(0,MAX_J):
            pt = Point( (i*50)+60, (j*50)+60 )
            pt2 = Point( (i*50)+100, (j*50)+100 )
            rect = Rectangle(pt,pt2)
            rect.setFill('white')
            rect.draw(win)

    for i in range(0,MAX_I):
        pt = Point( (i*50)+70, 40 )
        label = Text( pt, i)
        label.setTextColor('white')
        label.draw(win)
    for j in range(0,MAX_J):
        pt = Point( 40, (j*50)+70 )
        label = Text( pt, j)
        label.setTextColor('white')
        label.draw(win)

    for scale in range(0,4):
        text_pt = Point( (scale*50)+130, (MAX_J*50)+100 )
        pt = Point( (scale*50)+110, (MAX_J*50)+110 )
        pt2 = Point( (scale*50)+150, (MAX_J*50)+150 )
        rect = Rectangle(pt,pt2)

        if scale==3:
            label = Text( text_pt, "High")
            label.setTextColor('white')
            label.draw(win)
            rect.setFill('Red')
        elif scale==2:
            rect.setFill('Orange')
        elif scale==1:
            rect.setFill('Yellow')
        elif scale==0:
            label = Text( text_pt, "Low")
            label.setTextColor('white')
            label.draw(win)
            rect.setFill('Green')
        rect.draw(win)
            
def draw_objects(guess_matrix):
    for i in range(0,MAX_I):
        for j in range(0,MAX_J):
            #print("i: ",i,"j: ",j)
            #print(win.items[i*MAX_I + j])
            if guess_matrix[i][j].val==3:
                win.items[i*MAX_I + j].setFill('Red')
            elif guess_matrix[i][j].val==2:
                win.items[i*MAX_I + j].setFill('Orange')
            elif guess_matrix[i][j].val==1:
                win.items[i*MAX_I + j].setFill('Yellow')
            elif guess_matrix[i][j].val==0:
                win.items[i*MAX_I + j].setFill('Green')
            win.update()












    
MAX_I = 7
MAX_J = 7
my_matrix =[]
guess_matrix =[]

global win_x
global win_y
global win
win_x= MAX_I * 50 + 100
win_y= MAX_J * 50 + 200
win = GraphWin("My Window", win_x,win_y)
win.setBackground('black')


for i in range(0,MAX_I):
    new_row= []
    guess_row= []
    for j in range(0,MAX_J):
        new_node = node(0)
        guess_node = node("-")
        new_row.append( new_node )
        guess_row.append( guess_node )
        
    my_matrix.append(new_row)
    guess_matrix.append(guess_row)

for i in range(0, int((random.random()*3))+1):
    x = int(1+(random.random()*(MAX_I-2)))
    y = int(1+(random.random()*(MAX_J-2))) 
    #print( x, y )

    set_xy(my_matrix, x, y)
init_objects(guess_matrix)

while True:
    
    click = win.getMouse()
    guessX= click.getX()-50
    guessX /= 50
    guessY= click.getY()-50
    guessY /= 50
    
##    print("What is your guess")
##    guessX,guessY =input().split()
    guessX = int(guessX)
    guessY = int(guessY)

    print("Guess x: ",guessX, "guess y: ", guessY)
    guess_matrix[guessX][guessY] = my_matrix[guessX][guessY]
    value = my_matrix[guessX][guessY].val
    draw_objects(guess_matrix)
    if int(value) == int(3):
        break
    print_matrix(guess_matrix)
    

print("\nYou win!!!")
print_matrix(my_matrix)
draw_objects(my_matrix)

while True:
    pass

