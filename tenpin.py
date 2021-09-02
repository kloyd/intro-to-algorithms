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
    pins = input('Please enter number of pins down for ball ' + str(ball_in_frame) 
    + " in frame " + str(current_frame) + ": ")
    return int(pins)

def print_score():
    print_score = "|"
    print_frame = "|"
    pin_counter = 0
    frame_counter = 1
    game_score = 0
    frame_marker = "  " 
    while (frame_counter < 11):
        frame_score = 0
        frame_marker = "  " 
        if(pin_score[pin_counter] == 10):
            #strike, check next 2 pins
            frame_marker = "  |X| |"
            if(pin_score[pin_counter + 2] > -1):
                frame_score = pin_score[pin_counter] + pin_score[pin_counter + 1] + pin_score[pin_counter + 2]
            pin_counter = pin_counter + 1
        elif(pin_score[pin_counter] + pin_score[pin_counter + 1] == 10):
            #spare, check next pins
            frame_marker = "  |" + str(pin_score[pin_counter]) + "|/|"
            if(pin_score[pin_counter + 2] > -1):
                frame_score = pin_score[pin_counter] + pin_score[pin_counter + 1] + pin_score[pin_counter + 2]
            pin_counter = pin_counter + 2    
        else:
            if ((pin_score[pin_counter] > -1) & (pin_score[pin_counter + 1] > -1)):
                frame_score = pin_score[pin_counter] + pin_score[pin_counter + 1]
                frame_marker = "  |" + str(pin_score[pin_counter]) + "|" + str(pin_score[pin_counter + 1]) + "|"
            pin_counter = pin_counter + 2
        frame_counter = frame_counter + 1
        print_frame = print_frame + frame_marker
        print_score = print_score + " " + "{: >2d}".format(frame_score) + "   |"
        game_score = game_score + frame_score
    print_score = print_score + " game " + str(game_score)
    print(print_frame)
    print(print_score)


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
        if (pin_score[pin_pointer - 1] + pin_score[pin_pointer]) == 10:
            print ("Spare!")
        current_frame = current_frame + 1
        pin_pointer = pin_pointer + 1
    if current_frame == 11:
        # check if we need another pin score.
        # Was the previous pin score a Strike?
        if (pin_score[pin_pointer - 1] == 10):
            # Yes, we need 2 more pin scores.
            pin_score[pin_pointer] = get_pins(10, 2)
            pin_score[pin_pointer + 1] = get_pins(10, 3)
        # Was the 10th Frame a Spare?
        if (pin_score[pin_pointer - 1] + pin_score[pin_pointer - 2] == 10):
            # Yes, we need one more pin score.
            pin_score[pin_pointer] = get_pins(10, 3)
    print_score()

        
        


