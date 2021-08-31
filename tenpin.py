# Program to compute ten pin bowling scores

# 21 pin_score variables to hold number of pins knocked
# down by each ball bowled.
pin_score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frame_score = [0,0,0,0,0,0,0,0,0,0]
# 1 to 10 frames, start with frame 1
current_frame = 1
# pin_score position (0-20)
pin_pointer = 0
ball_in_frame = 1

def get_pins(current_frame, ball_in_frame):
    pins = input('Please enter number of pins down for ball ' + str(ball_in_frame) + " in frame " + str(current_frame) + " :")
    return pins

while current_frame < 11:
    pins = get_pins(current_frame,ball_in_frame)
    if pins == 10:
        print ("Strike!")
        pin_score[pin_pointer] = pins
        current_frame = current_frame + 1
    else:
        ball_in_frame = 2
        pin_pointer = pin_pointer + 1
        pins = get_pins(current_frame, ball_in_frame)
        if (pin_score[pin_pointer - 1] + pins) == 10:
            print ("Spare!")

