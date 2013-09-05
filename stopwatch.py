# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
interval = 100
total_time = 0
attempts = 0
wins = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(int):
    if int < 10:
        a = 0
        b = 0
        c = 0
        d = str(int)[0]
        return str(a) + ":" + str(b) + str(c) + '.' + d
    elif 10 <= int < 100:
        a = 0
        b = 0
        c = str(int)[0]
        d = str(int)[1]
        return str(a) + ":" + str(b) + str(c) + '.' + d
    elif 100 <= int < 600:
        a = 0
        b = str(int)[0]
        c = str(int)[1]
        d = str(int)[2]
        return str(a) + ":" + str(b) + str(c) + '.' + d
    elif 600 <= int < 10000:
        min = (int // 600)
        sec = (int // 10) % 60
        hund = (int)
        b = str(sec)
        d = str(hund)[-1]
        if len(str(sec)) == 2:
            return str(min) + ":" + str(b) + '.' + d
        else:
            return str(min) + ":" + "0" + str(b) + '.' + d

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global is_running
    timer.start()
    is_running = True
    
    
def stop_handler():
    global attempts, wins, total_time, is_running
    attempts += 1
    if is_running == True and str(total_time)[-1] == '0':
        wins += 1
    timer.stop()
    is_running = False
    
def reset_handler():
    global total_time, attempts, wins
    timer.stop
    total_time = 0
    attempts = 0
    wins = 0

    
# define event handler for timer with 0.1 sec interval
def tick():
    global total_time, str_time
    total_time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(total_time), (100, 100), 20, "white")
    canvas.draw_text(str(attempts), (150, 45), 18, "white")       
    canvas.draw_text('/' + str(wins), (185, 45), 18, "white")
    canvas.draw_text('Attempts', (120, 20), 18, "white")       
    canvas.draw_text('Wins', (195, 20), 18, "white")
       
# create frame
frame = simplegui.create_frame("Timer", 300, 300)
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)


# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()
