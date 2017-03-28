# Thomas Khuu
# June 2015 - July 2015

import simplegui

starter = "0:00.0"
counter = 0
x = 0
y = 0

# helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global starter, x, y
    
    timer.stop()
    if timer.is_running():
        y += 1
        starter = format(counter)
        if starter[-1] == '0': x += 1

def reset():
    global starter, counter, x, y
    timer.stop()
    starter = "0:00.0"
    counter = 0
    x = 0
    y = 0
    
# event handler for timer with 0.1 sec interval
def timer():
    global counter
    counter += 1
    
# draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [100, 110], 40, "White")
    canvas.draw_text(str(x) + "/" + str(y), [230, 35], 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, timer)

frame.start()
