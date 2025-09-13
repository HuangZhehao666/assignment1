# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 15:05:07 2025

@author: Lenovo
"""
import turtle
import random
import time
import tkinter as tk  #Handle the underlying Tkinter resource cleanup

def draw_tree():
    # Forcibly clean up underlying residual resources
    try:
        # Reset the turtle running flag to avoid the terminated state
        turtle.TurtleScreen._RUNNING = True
        # Trigger Tkinter resource recycling to clean up possible residual root windows
        temp_root = tk.Tk()
        temp_root.destroy()
    except Exception:
        pass  
    
    # Create an independent screen
    screen = turtle.Screen()
    screen.screensize(bg='white')  
    # Creare Turtle
    t = turtle.Turtle()
    t.hideturtle()  # Hide the pen
    screen.tracer(5, 0)  # Refresh once every 5 steps
    
    # Recursive tree-drawing function
    def Tree(branch):
        time.sleep(0.0005)
        if branch > 3:
            # Logic for branch color and thickness
            if 8 <= branch <= 12:
                t.color('lightgreen' if random.randint(0, 2) == 0 else 'darkgreen')
                t.pensize(branch / 3)
            elif branch < 8:
                t.color('lightgreen' if random.randint(0, 1) == 0 else 'green')
                t.pensize(branch / 2)
            else:
                t.color('sienna')
                t.pensize(branch / 10)
            
            # Draw the current branch and recursively draw sub-branches
            t.forward(branch)
            a = 1.5 * random.random()
            t.right(20 * a)
            b = 1.5 * random.random()
            Tree(branch - 10 * b)
            t.left(40 * a)
            Tree(branch - 10 * b)
            t.right(20 * a)
            t.penup()
            t.backward(branch)
            t.pendown()
    
    # Initialize the brush position (with the tree trunk facing upward)
    t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()
    t.color('sienna')
    # Draw the tree and wait for closure
    Tree(60)
    screen.update()  # Ensure all graphics are fully displayed
    screen.exitonclick()  # Automatically close the canvas and destroy resources after a click

def draw_smile():
    # Same as drawing a tree
    try:
        turtle.TurtleScreen._RUNNING = True
        temp_root = tk.Tk()
        temp_root.destroy()
    except Exception:
        pass
    
    # Create an independent screen and set an appropriate size 
    # to make sure the smiley face is displayed in the center
    screen = turtle.Screen()
    screen.setup(500, 500, 0, 0) 
    screen.bgcolor('white')       
    t = turtle.Turtle()
    t.speed(5)  
    t.hideturtle()  

    # Draw the yellow face (circular shape, filled with yellow)
    t.penup()
    t.goto(0, -150)  # Move to the bottom of the face (to facilitate drawing a circle with its center at (0, 0))
    t.pendown()
    t.color('black', 'yellow')  # Black outline, yellow fill
    t.begin_fill()
    t.circle(150)  # Draw a circle with a radius of 150 (size of the face)
    t.end_fill()

    # Draw the left eye 
    t.penup()
    t.goto(-60, 30)  # Left eye coordinates: 60 left, 30 up (relative to the center of the face)
    t.pendown()
    t.color('black', 'black')  # fill with black
    t.begin_fill()
    t.circle(20)  # Eye radius: 20
    t.end_fill()

    # Draw the right eye 
    t.penup()
    t.goto(60, 30)  # Right eye coordinates: 60 right, 30 up (relative to the center of the face)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # Draw the mouth
    t.penup()
    t.goto(-70, -40)  # Position of the left corner of the mouth
    t.pendown()
    t.color('black')
    t.pensize(5)
    t.setheading(-90)  # The brush direction is downward
    t.circle(70, 180)  # Draw a downward arc with a radius of 70 and an angle of 180 degrees

    screen.exitonclick()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for tree, 2 for smile, 3 to exit)\n"
              "Your selection is: ")
    try:
        a = int(a)
        if a == 1:
            draw_tree()
        elif a == 2:
            draw_smile()
        elif a == 3:  
            print("Program exited successfully!")
            break  # Exit the loop and terminate the program
        else:
            print("Please input the value in [1,2,3]")
    except ValueError:
        print("Please input the value in [1,2,3]")
