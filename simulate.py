import numpy as np
import sys
from utils import readFile,preprocessCommands

if len(sys.argv) != 2:
        "please pass the file of the commands"
        exit(0)
# Using functions from Utils to read command input text file
Commands = readFile(sys.argv[1])

global D
D = ["NORTH", "EAST", "SOUTH", "WEST"]
global orientation

# defining a function for keeping track of direction
def direction():
    
    global pointer
    global orientation
    global facing
    
    if facing == "NORTH":
        temp = 1
    if facing == "EAST":
        temp = 2
    if facing == "SOUTH":
        temp = 3
    if facing == "WEST":
        temp = 4
        
    pointer = temp
    orientation = D[pointer-1]

# Function to turn right
def right():
    global facing      
    global pointer
    pointer = pointer%4 + 1
    if pointer == 1:
            facing = "NORTH"
    if pointer == 2:
            facing = "EAST"
    if pointer == 3:
            facing = "SOUTH"
    if pointer == 4:
            facing = "WEST"
    
# Function to turn left
def left():
    global facing    
    global pointer

    pointer = pointer%4 - 1
    if pointer == 1:
            facing = "NORTH"
    if pointer == 2:
            facing = "EAST"
    if pointer == 3:
            facing = "SOUTH"
    if pointer == 4:
            facing = "WEST"       
        

# Function to report the values
def report():
    global X
    global Y
    global pointer
    global D
    print("Output =",X,Y,D[pointer-1])

# Function for move command    
def move():
    global X
    global Y
    global pointer
    
    
    if (pointer == 1):
        Y = Y + 1
        if (Y > 4):
                Y = Y - 1
    if (pointer == 2):
        X = X + 1
        if (X > 4):
                X = X - 1
    if (pointer == 3):
        Y = Y - 1
        if (Y < 0):
                Y = Y + 1
    if (pointer ==4):
        X = X - 1
        if (X < 0):
                X = X + 1
    
print("Commands given =",Commands)

# conditions to check if the first command is Place command
if "PLACE" not in Commands[0]:
        print("The first valid command to the robot is a PLACE command, please specify it")

elif "PLACE" in Commands[0]:
            # Looping over the commands for execution
            for command in Commands:
                global X
                global Y
                global facing
                global orientation
                if "PLACE" in command:
                    # parse details of place commands to global variables    
                    command_splitted = preprocessCommands(command)
                    X = int(command_splitted[0])
                    Y = int(command_splitted[1])
                    facing = command_splitted[2]
                   
                if "MOVE" in command:
                        direction()
                        move()
                        
                if "LEFT" in command:
                        direction()
                        left()
                        
                if "RIGHT" in command:
                        direction()
                        right()

                if "REPORT" in command:
                        report()               
