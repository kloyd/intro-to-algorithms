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
format_spaces = "_" * 3
score_card_frames = ""
i = 1
while (i < 11):
    score_card_frames = score_card_frames + format_spaces + str(i) + format_spaces
    i = i + 1
score_card_frames = score_card_frames + format_spaces * 4 + "_"
score_card_footer = format_spaces * 28

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
            # This is a Strike, check next 2 pins.
            # If there are pin scores recorded (the pin score is not -1)
            # then add them up.
            
            frame_marker = "  |X"
            if(pin_score[pin_counter + 2] > -1):
                frame_score = pin_score[pin_counter] + pin_score[pin_counter + 1] + pin_score[pin_counter + 2]
                if(frame_counter == 10):
                    # There is a strike in Frame 10, show the next two pin scores as well.
                    # Extra stuff not really needed for the computation part of our Algorithm.
                    # This is actually User Interface code.
                    # Which means, give the User something meaninful to look at.
                    # in this case we are emulating what a regular bowling
                    # score sheet looks like.
                    extra_pin_1 = pin_score[pin_counter + 1]
                    extra_pin_2 = pin_score[pin_counter + 2]
                    if(extra_pin_1 == 10):
                        frame_marker =  frame_marker + "|X"
                    else:
                        frame_marker = frame_marker + "|" + str(extra_pin_1)
                    if(extra_pin_2 == 10):
                        frame_marker = frame_marker + "|X"
                    else:
                        frame_marker = frame_marker + "|" + str(extra_pin_2)
                    frame_marker = frame_marker + "|"
                else:
                    frame_marker = frame_marker + "| |"
            # A Strike will move our pin position up by one!
            pin_counter = pin_counter + 1
        elif(pin_score[pin_counter] + pin_score[pin_counter + 1] == 10):
            #spare, check next pins
            frame_marker = "  |" + str(pin_score[pin_counter]) + "|/|"
            if(pin_score[pin_counter + 2] > -1):
                pin_1 = pin_score[pin_counter]
                pin_2 = pin_score[pin_counter + 1]
                pin_3 = pin_score[pin_counter + 2]
                frame_score = pin_1 + pin_2 + pin_3
                if (frame_counter == 10):
                    # Special output for the Frame score ... |n|/|n|
                    # e.g. |7|/|5|
                    if (pin_3 == 10):
                        # mark strike with an X
                        display_pin = "X"
                    else:
                        display_pin = str(pin_3)
                    frame_marker = frame_marker + display_pin + "|"
            # A spare will use 2 pin scores, move up by two!
            pin_counter = pin_counter + 2    
        else:
            if ((pin_score[pin_counter] > -1) & (pin_score[pin_counter + 1] > -1)):
                frame_score = pin_score[pin_counter] + pin_score[pin_counter + 1]
                frame_marker = "  |" + str(pin_score[pin_counter]) + "|" + str(pin_score[pin_counter + 1]) + "|"
            # Any other score for a frame is just the two pins added up
            # and so we move our pin counter up by 2 for the next frame.
            pin_counter = pin_counter + 2
        #
        # We are all done with the current Frame, move up to the next Frame.
        frame_counter = frame_counter + 1
        print_frame = print_frame + frame_marker
        if (frame_counter == 11):
            print_score = print_score + "   " 
        else:
            print_score = print_score + " "
        print_score = print_score + "{: >2d}".format(frame_score) + "   |"
        game_score = game_score + frame_score
    print_score = print_score + " Total " + str(game_score)
    print()
    print(score_card_frames)
    print(print_frame)
    print(print_score)
    print(score_card_footer)


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

        
        


