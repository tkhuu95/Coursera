# Thomas Khuu
# June 2015 - July 2015

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HALF_PAD_HEIGHT
paddle2_pos = HALF_PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    vertical = random.randrange(60, 180) / 60.0
    horizontal = random.randrange(120, 240) / 60.0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction: ball_vel = [horizontal, vertical]
    elif not direction: ball_vel = [vertical, horizontal]
        
# event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HALF_PAD_HEIGHT
    paddle2_pos = HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(random.choice([LEFT, RIGHT]))
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #keep ball from leaving top and bottom of canvas 
    if ball_pos[1] <= BALL_RADIUS: ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] >= HEIGHT - BALL_RADIUS: ball_vel[1] = - ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT: paddle1_pos += paddle1_vel
        
    if paddle1_pos + paddle1_vel >= HEIGHT - 20: paddle1_pos -= paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT: paddle2_pos += paddle2_vel
        
    if paddle2_pos + paddle2_vel >= HEIGHT - 20: paddle2_pos -= paddle2_vel
        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                     [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                                                    PAD_WIDTH, "White")
    
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                                                    PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - 1.125 * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score2 += 1
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - 1.125 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score1 += 1
        
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, 45], 45, "White")
    canvas.draw_text(str(score2), [WIDTH - 150, 45], 45, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    acc = 10
    if key == simplegui.KEY_MAP["s"]: paddle1_vel += acc
    
    elif key == simplegui.KEY_MAP["w"]: paddle1_vel -= acc
    
    if key == simplegui.KEY_MAP["up"]: paddle2_vel -= acc
        
    elif key == simplegui.KEY_MAP["down"]: paddle2_vel += acc
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    acc = -10
    if key == simplegui.KEY_MAP["s"]: paddle1_vel += acc
    
    elif key == simplegui.KEY_MAP["w"]: paddle1_vel -= acc
    
    if key == simplegui.KEY_MAP["up"]: paddle2_vel -= acc
        
    elif key == simplegui.KEY_MAP["down"]: paddle2_vel += acc
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
