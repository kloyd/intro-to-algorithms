# Program to compute ten pin bowling scores

# 21 pin_score variables to hold number of pins knocked
# down by each ball bowled.
# Start with -1 to indicate that no pin score has been made yet.
pin_score = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
frame_score = [0,0,0,0,0,0,0,0,0,0]
# 1 to 10 frames, start with frame 1
current_frame = 1
# pin_score position (0-20)
pin_pointer = 0
ball_in_frame = 1

def get_pins(current_frame, ball_in_frame):
    pins = input('Please enter number of pins down for ball ' + str(ball_in_frame) + " in frame " + str(current_frame) + ": ")
    return int(pins)

while current_frame < 11:
    ball_in_frame = 1
    pins = get_pins(current_frame, ball_in_frame)
    pin_score[pin_pointer] = pins
    if pins == 10:
        print ("Strike!")
        
        pin_pointer = pin_pointer + 1
        current_frame = current_frame + 1
    else:
        ball_in_frame = 2
        pin_pointer = pin_pointer + 1
        pins = get_pins(current_frame, ball_in_frame)
        pin_score[pin_pointer] = pins
        print(pin_score[pin_pointer], pin_score[pin_pointer - 1])
        if (pin_score[pin_pointer - 1] + pin_score[pin_pointer]) == 10:
            print ("Spare!")
        current_frame = current_frame + 1
    if current_frame == 11:
        # check if we need another pin score.
        # Was the previous pin score a Strike?
        if (pin_score[pin_pointer - 1] == 10):
            # Yes, we need 2 more pin scores.
            pin_score[pin_pointer + 1] = get_pins(10, 2)
            pin_score[pin_pointer + 2] = get_pins(10, 3)
        # Was the 10th Frame a Spare?
        if (pin_score[pin_pointer] + pin_score[pin_pointer - 1] == 10):
            # Yes, we need one more pin score.
            pin_score[pin_pointer + 1] = get_pins(10, 3)


        
        


