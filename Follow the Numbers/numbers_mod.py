# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:50:09 2022

@author: chris.pham
@modified: Shivansh Shukla
"""

# Import necessary libraries and modules
import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint
import time

# Set the width and height of the game window
WIDTH = 400
HEIGHT = 500

# Create an Actor object named "dot" for debugging
dot = Actor("dot")

# Set up lists to store dots and lines
dots = []
lines = []

# variable to store the number of misses
miss = 0

# current level is set to 1
curr_lev =1

# game over boolean for checking game over or not
game_over = False
win = False

# Initialize the variable to keep track of the next dot to connect
next_dot = 0

#random dots to be created on screen each time code runs
rand_dots_seq1 = randint(3, 6)

# start and end times for the levels
start_time_lev1 = 0
start_time_lev2 = 0
start_time_lev3 = 0
end_time_lev1 = 0
end_time_lev2 = 0
end_time_lev3 = 0

# Generate and position seven random dots on the screen
for dot in range(0, rand_dots_seq1):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
    dots.append(actor)

# The draw function is called to render the game screen
def draw():
    # Fill the screen with a dark blue color (navy blue)
    screen.fill((0, 0, 128))
    
    # Initialize a variable to number the dots
    dot_number = 1
    
    if game_over:
        # Display a red screen and a game over message
        screen.fill('red')
        screen.draw.text("You Lost!", center=(WIDTH/2, HEIGHT/2), fontsize=60, color='black')
    
    elif win:
        # Display a white screen, a message indicating the completion of all levels,
        # and the time taken for each level
        screen.fill('white')
        screen.draw.text(f"You Finished All Levels!", center=(WIDTH/2, 20), fontsize=50, color='black')
        screen.draw.text(f"Time level 1: {(end_time_lev1 - start_time_lev1):.2f}s", center=(WIDTH/2, HEIGHT/2), fontsize=30, color='black')
        screen.draw.text(f"Time level 2: {(start_time_lev3 - start_time_lev2):.2f}s", center=(WIDTH/2, HEIGHT/2 + 20), fontsize=30, color='black')
        screen.draw.text(f"Time level 3: {(end_time_lev3 - start_time_lev3):.2f}s", center=(WIDTH/2, HEIGHT/2 + 40), fontsize=30, color='black')
        
    else:
        # Iterate through the dots and draw them on the screen
        for dot in dots:
            # Display the dot number near each dot
            screen.draw.text(str(dot_number), (dot.pos[0], dot.pos[1] + 10))
            screen.draw.text(f"Misses: {miss}", topleft=(0, 0))
            dot.draw()
            dot_number = dot_number + 1
        
        # Iterate through the lines and draw them on the screen
        for line in lines:
            # Draw lines with a color specified as (200, 200, 100)
            screen.draw.line(line[0], line[1], (200, 200, 100))
                
        
# Function to handle the transition to the next level
def level_2():
    global next_dot
    
    # Clear the lists of dots and lines
    dots.clear()
    lines.clear()
    
    next_dot = 0  # Reset the next dot to connect
    
    # Generate and position dots for level 2
    for _ in range(0, rand_dots_seq1 + 2):
        actor = Actor("red-dot")
        actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
        dots.append(actor)
        
        
def level_3():
    global next_dot
    
    # Clear the lists of dots and lines
    dots.clear()
    lines.clear()
    
    next_dot = 0  # Reset the next dot to connect
    
    # Generate and position dots for level 3
    for i in range(0, rand_dots_seq1 + 4):
        if (i < (rand_dots_seq1 + 4) / 2):
            actor = Actor('dot')
            actor.pos = randint(20, WIDTH/2), randint(20, HEIGHT - 20)
        else:
            actor = Actor('red-dot')
            actor.pos = randint(WIDTH/2, WIDTH-20), randint(20, HEIGHT - 20)
        
        dots.append(actor)
        
    
# The on_mouse_down function is called when the mouse button is clicked
def on_mouse_down(pos):
    global next_dot
    global miss
    global game_over, win
    global lines
    global curr_lev 
    global start_time_lev2, start_time_lev1, start_time_lev3
    global end_time_lev1, end_time_lev2, end_time_lev3
    
    # Check if the number of misses has reached the maximum (4)
    if miss == 4:
        # If the player has missed too many times, set the game over flag
        game_over = True
        return game_over
    
    # Check if the clicked point collides with the current dot and if the player hasn't missed too many times
    if dots[next_dot].collidepoint(pos) and miss < 4:
        if next_dot:
            # If it's not the first dot successfully clicked, add a line connecting the previous dot to the current dot
            lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
        
    else:
        # If the click doesn't hit the current dot or misses exceed the limit, reset the lines and next_dot, and increment miss by 1
        lines = []
        next_dot = 0
        miss += 1
    
    # Check if all dots for the current level have been successfully clicked
    if next_dot == len(dots):
        # Record the completion time for the current level based on the current level number
        if curr_lev == 1:
            end_time_lev1 = time.time()
        
        # Move to the next level
        curr_lev += 1
        
        # Depending on the current level, initialize the next level's setup
        if curr_lev == 2:
            level_2()
            start_time_lev2 = time.time()
        elif curr_lev == 3:
            level_3()
            start_time_lev3 = time.time()
        else:
            # If all levels are completed, set the win flag and record the completion time for the final level
            win = True
            end_time_lev3 = time.time()

            
start_time_lev1 = time.time()     
    
# Start the Pygame Zero game loop
pgzrun.go()
