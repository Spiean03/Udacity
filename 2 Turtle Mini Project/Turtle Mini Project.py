# -*- coding: utf-8 -*-

import turtle
import numpy as _n

def draw_figure(number_of_edges):
    number_of_degrees= (number_of_edges-2)*180
    print(number_of_degrees)
    degrees_per_edge=float(number_of_degrees/number_of_edges)
    print degrees_per_edge
    window = turtle.Screen()
    window.bgcolor("red")
    brad =turtle.Turtle()
    start = 1
    while start <= number_of_edges:
        brad.forward(5)
        brad.right(180-degrees_per_edge)
        start += 1
    window.exitonclick()
    
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in (1,5):
        brad.forward(100)
        brad.right(90)
        
    #Create the turtle Angie - draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    window.exitonclick()
    
def draw_circle_from_squares(size,number_of_squares):
    window = turtle.Screen()
    window.bgcolor("red")
    pipa = turtle.Turtle()
    pipa.shape('arrow')
    pipa.color("white")
    for i in range(1,number_of_squares):
        pipa.forward(size/2)
        for i in range(1,4):
            pipa.right(90)
            pipa.forward(size)
        pipa.right(90)
        pipa.forward(size/2)
        pipa.right(float(360/number_of_squares))
    window.exitonclick()


def draw_flower(): #This code draws the flower
    window =turtle.Screen()
    window.bgcolor("white")

    mosaique=turtle.Turtle()
    mosaique.shape('circle')
    mosaique.speed('fastest')
    mosaique.shapesize(0.5,0.5)
    mosaique.color("blue")
    mosaique.begin_fill()

    for i in range (72):
        draw_square(mosaique)
        mosaique.right(5)
    mosaique.end_fill
    mosaique.right(90)
    mosaique.forward(330)
    window.exitonclick()
    
    
def draw_miniGreenTriangle(some_turtle):
    some_turtle.right(60)
    some_turtle.forward(30)
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.right(120)
    some_turtle.forward(30)

def draw_oneset(tuffy):
    tuffy.begin_fill()
    draw_miniGreenTriangle(tuffy)    
    tuffy.penup()
    tuffy.right(120)
    tuffy.forward(30)
    tuffy.left(60)
    tuffy.pendown()
    draw_miniGreenTriangle(tuffy)
    tuffy.penup()
    tuffy.left(120)
    tuffy.forward(30)
    tuffy.right(180)
    tuffy.pendown()
    draw_miniGreenTriangle(tuffy)
    tuffy.end_fill()

def draw_largerModule(some_turtle3,headvalue,posvalue):
    for i in range(0,4):
        some_turtle3.penup()
        some_turtle3.setpos(posvalue)
        some_turtle3.setheading(headvalue)        
        some_turtle3.forward(60*i)
        some_turtle3.pendown()
        draw_oneset(some_turtle3)
    
def draw_mainShape():   # this code draws the green triangles
    window = turtle.Screen()
    window.bgcolor = 'white'        
    basicTurtle = turtle.Turtle('turtle')
    basicTurtle.speed(10)
    basicTurtle.color('blue')
    basicTurtle.fillcolor('green')
    draw_largerModule(basicTurtle,0,(0,0))   
    for i in range(0,2):
        basicTurtle.back(30)
        basicTurtle.left(60)
        newpos = basicTurtle.pos()
        newhead = basicTurtle.heading()
        draw_largerModule(basicTurtle,newhead,newpos)
    window.exitonclick()     
    
def draw_kc():
    window = turtle.Screen()
    window.bgcolor = 'white'        
    k = turtle.Turtle('turtle')
    k.speed(10)
    k.color('blue')
    k.left(90)
    k.forward(100)
    k.backward(50)
    k.right(45)
    k.forward(int(100/_n.sqrt(2)))
    k.backward(int(100/_n.sqrt(2)))
    k.right(90)
    k.forward(int(100/_n.sqrt(2)))
    print k.position()
    k.color(window.bgcolor)
    k.goto(99.50,0.50)
    k.color("blue")
    k.left(45)
    k.forward(50)
    k.backward(50)
    k.left(90)
    k.forward(100)
    k.right(90)
    k.forward(50)
    window.exitonclick()


#To draw the flower, execute draw_flower()
#To draw the green triangles, execute draw_mainShape()
#To draw the KC logo, execute draw_kc. Important note: I've added the sqrt from numpy, so you need to add square root function from numpy (import numpy as _n)
