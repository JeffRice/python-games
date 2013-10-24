# implementation of card game - Memory

import simplegui
import random

counter = 0
deck = range(8) * 2
random.shuffle(deck)
range(len(deck))
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,]
state = 0
flipped_1 = []
flipped_2 = []
expos = []
expos2 = []
moves = 0

# helper function to initialize globals
def init():
    global state, deck, deck_num, exposed, card_index, flipped_1, flipped_2, moves
    moves = 0
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,]
    label.set_text("Moves = " + str(moves))
    random.shuffle(deck)
    state = 0
    
    
# define event handlers
def mouseclick(pos):
    global state, deck, deck_num, exposed, card_index, flipped_1, flipped_2, expos, expos2, moves
    # add game state logic here
    x = pos[0] // 50
    if state == 0:
        if exposed[x] == False:
            exposed[x] = True
            flipped_1 = deck[x]
            expos = pos[0] // 50
            state = 1
        else:
            state = 0
    elif state == 1:
        if exposed[x] == False:
            exposed[x] = True
            flipped_2 = deck[x]
            expos2 = pos[0] // 50
            state = 2
        else:
            state = 1
    else:
        if exposed[x] == False:
            exposed[x] = True
            if flipped_1 == flipped_2:
                print 'match'
            else:
                exposed[expos] = False
                exposed[expos2] = False
            flipped_1 = deck[x]
            expos = pos[0] // 50
            state = 1  
            moves += 1
            label.set_text("Moves = " + str(moves)) 
        else:
            state = 2
     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, deck_num, exposed, card_index
    pos = -25
    for card_index in range(len(deck)):
        if exposed[card_index]:
        # contained true so display card
            pos += 50
            canvas.draw_text(str(deck[card_index]), (card_index * 50 + 10, 60), 48, "White")     # deck[card_index] is the value of the card at this index position
        else:
            pos += 50
            canvas.draw_polygon([(pos, 0), (pos, 100)], 50, "green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = " + str(moves))

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric