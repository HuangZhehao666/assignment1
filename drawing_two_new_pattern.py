# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 15:05:07 2025

@author: Lenovo
"""
import turtle
import random
import time
import tkinter as tk  

def draw_tree():
    try:
        turtle.TurtleScreen._RUNNING = True
        temp_root = tk.Tk()
        temp_root.destroy()
    except Exception:
        pass  
    
    screen = turtle.Screen()
    screen.screensize(bg='white')  
    
    t = turtle.Turtle()
    t.hideturtle()  
    screen.tracer(5, 0)  
    
    def Tree(branch):
        time.sleep(0.0005)
        if branch > 3:
            if 8 <= branch <= 12:
                t.color('lightgreen' if random.randint(0, 2) == 0 else 'darkgreen')
                t.pensize(branch / 3)
            elif branch < 8:
                t.color('lightgreen' if random.randint(0, 1) == 0 else 'green')
                t.pensize(branch / 2)
            else:
                t.color('sienna')
                t.pensize(branch / 10)
            
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
    
    t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()
    t.color('sienna')
    
    Tree(60)
    screen.update()  
    screen.exitonclick()  

def draw_smile():
    try:
        turtle.TurtleScreen._RUNNING = True
        temp_root = tk.Tk()
        temp_root.destroy()
    except Exception:
        pass
    
    screen = turtle.Screen()
    screen.setup(500, 500, 0, 0) 
    screen.bgcolor('white')       
    t = turtle.Turtle()
    t.speed(5)  
    t.hideturtle()  

   
    t.penup()
    t.goto(0, -150)  
    t.pendown()
    t.color('black', 'yellow')  
    t.begin_fill()
    t.circle(150)  
    t.end_fill()

    
    t.penup()
    t.goto(-60, 30)  
    t.pendown()
    t.color('black', 'black')  
    t.begin_fill()
    t.circle(20)  
    t.end_fill()


    t.penup()
    t.goto(60, 30)  
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()


    t.penup()
    t.goto(-70, -40)  
    t.pendown()
    t.color('black')
    t.pensize(5)
    t.setheading(-90)  
    t.circle(70, 180)  

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
            break  
        else:
            print("Please input the value in [1,2,3]")
    except ValueError:
        print("Please input the value in [1,2,3]")