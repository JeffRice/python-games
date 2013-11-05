elper function that spawns a ball by updating the 
# ball's position vector and velocity vector
77;10103;0c# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        vel[0] = random.randrange(120,240) / -100
        vel[1] = random.randrange(60, 180) / -100
    else:
        vel[0] = random.randrange(120,240) / 100
        vel[1] = random.randrange(60,180) / -100
    

        # define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    roll = random.randrange(0, 2)
    if roll == 1:
        right = True
    else:
        right = False
    ball_init(right)

def reset():
    global score1, score2
    score1 = 0
    score2 = 0 
    new_game()
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, vel, HEIGHT

    # update paddle's vertical position, keep paddle on the screen


    paddle1_pos[0] += paddle1_vel[0]
    paddle1_pos[1] += paddle1_vel[1]

    if paddle1_pos[1] > HEIGHT:
        paddle1_pos[0] = HEIGHT - 80
        paddle1_pos[1] = HEIGHT
        
    if paddle1_pos[0] < 0:
        paddle1_pos[0] = 0
        paddle1_pos[1] = 80

        
    paddle2_pos[0] += paddle2_vel[0]
    paddle2_pos[1] += paddle2_vel[1]
    
    if paddle2_pos[1] > HEIGHT:
        paddle2_pos[0] = HEIGHT - 80
        paddle2_pos[1] = HEIGHT
        
    if paddle2_pos[0] < 0:
        paddle2_pos[0] = 0
        paddle2_pos[1] = 80
    
        
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([4, paddle1_pos[0]], [4, paddle1_pos[1]], 8, "White")
    c.draw_line([596, paddle2_pos[0]], [596, paddle2_pos[1]], 8, "White")    
        
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    if ball_pos[1] <= 0:
        vel[1] = -vel[1]
        
    if ball_pos[1] >= 400:
        vel[1] = -vel[1]
        
    if ball_pos[0] <= 8:
        if paddle1_pos[1] - ball_pos[1] >=0 and paddle1_pos[1] - ball_pos[1] <= 80:
            vel[0] = -vel[0] - (vel[0] *.1)
        else:
            score1 += 1
            right = False
            ball_init(right)

        
    if ball_pos[0] >= 592:
        if paddle2_pos[1] - ball_pos[1] >=0 and paddle2_pos[1] - ball_pos[1] <= 80:
            vel[0] = -vel[0] - (vel[0] *.1)
        else:
            score2 += 1
            right = True
            ball_init(right)
    
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score2), (350, 20), 16, "white")   
    c.draw_text(str(score1), (240, 20), 16, "white")
   
paddle1_pos = [160, 240]
paddle2_pos = [160, 240]    
    
def keydown(key):
    global paddle1_vel, paddle2_vel, HEIGHT, pad_speed
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += pad_speed
        paddle1_vel[1] += pad_speed
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= pad_speed
        paddle1_vel[1] -= pad_speed
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += pad_speed
        paddle2_vel[1] += pad_speed
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= pad_speed
        paddle2_vel[1] -= pad_speed
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    pad_speed = 3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[0] -= pad_speed
        paddle1_vel[1] -= pad_speed
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[0] += pad_speed
        paddle1_vel[1] += pad_speed
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[0] -= pad_speed
        paddle2_vel[1] -= pad_speed
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[0] += pad_speed
        paddle2_vel[1] += pad_speed

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button("Restart", reset, 70)

# start frame
frame.start()
new_game()
