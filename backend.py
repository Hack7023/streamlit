
import turtle

def canvas_builder(title, canvas_width, canvas_height):
    if(title=='star'):

        CANVAS_COLOR = "red"
        PEN_COLOR = "black"
        scr = turtle.Screen()
        scr.screensize(canvas_width, canvas_height)
        scr.title(title)
        scr.bgcolor(CANVAS_COLOR)
        turtle.setworldcoordinates(10, 10, canvas_width, canvas_height)
        t = turtle.Turtle()
        t.color(PEN_COLOR)
        t.begin_fill()
        po=0
        t.penup()
        t.goto(200,200)
        t.pendown()
        while po<1000:
            t.forward(200)
            t.left(170)
            po+=1
        
        t.end_fill()
        turtle.done()
    if(title=='square'):
        CANVAS_COLOR = "red"
        PEN_COLOR = "black"
        scr = turtle.Screen()
        scr.screensize(canvas_width, canvas_height)
        scr.title(title)
        scr.bgcolor(CANVAS_COLOR)
        turtle.setworldcoordinates(0, 0, canvas_width, canvas_height)
        t = turtle.Turtle()
        t.color(PEN_COLOR)
        t.begin_fill()
        for i in range(4):
            t.forward(10)
            t.left(90)
        t.end_fill()
        turtle.done()
