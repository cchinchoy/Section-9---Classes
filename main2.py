# -*- coding: utf-8 -*-
"""
    Project name : Import Assignment
    File name : main2.py
    Programmer : Colin B. Chin Choy
"""


import turtle
import random

k = turtle.Turtle()
TRACKS = 5
DISTANCE = 600
ANGLE = 90
HEIGHT = 50
BACKGROUND = "green"
LINE_COLOR = "white"
ri = []
r = "racer "
X_ORIGIN_POS = 0
Y_ORIGIN_POS = 0
X_FIRST_POS = 0
Y_FIRST_POS = 0
PLAYER_COLORS  = ["red","green","blue","orange","purple","pink","yellow"]

def startLine():
    global X_FIRST_POS
    global Y_FIRST_POS
    k.penup()
    k.back(300)
    k.right(ANGLE)
    k.fd(100)
    k.left(ANGLE)
    k.pendown()
    X_ORIGIN_POS = k.xcor()
    Y_ORIGIN_POS = k.ycor()
    print(X_ORIGIN_POS,Y_ORIGIN_POS)
    X_FIRST_POS = X_ORIGIN_POS+5
    Y_FIRST_POS = Y_ORIGIN_POS+25
    print(X_FIRST_POS,Y_FIRST_POS)

def racerCount(tracks):
    qty_racers = tracks

# def deployRacers(tracks):
#     racers = tracks
#     for i in range(racers):
#         name = r+str(i)
#         print(name)
#         print(Y_FIRST_POS)
# #        ri.append(name)
#         name = turtle.Turtle()
#         name.shape("turtle")
#         name.color("red")
#         name.goto(X_FIRST_POS,Y_FIRST_POS)
#         Y_FIRST_POS = Y_FIRST_POS+100


def buildTrack(trackcount):
    TRACKS = trackcount
    for i in range(TRACKS):
        k.forward(DISTANCE)
        k.left(ANGLE)
        k.forward(HEIGHT)
        k.left(ANGLE)
        k.forward(DISTANCE)
        k.left(ANGLE)
        k.forward(HEIGHT)
        k.penup()
        k.back(HEIGHT)
        k.left(ANGLE)
        k.pendown()

def playerColors():


startLine()
buildTrack(TRACKS)
# deployRacers(TRACKS)
racers = TRACKS
for i in range(racers):
    color = random.choice(PLAYER_COLORS)
    name = r+str(i)
    print(name)
    print(X_FIRST_POS)
    print(Y_FIRST_POS)
#        ri.append(name)
    name = turtle.Turtle()
    name.shape("turtle")
    name.penup()
    name.color("red")
    name.goto(X_FIRST_POS,Y_FIRST_POS)
    Y_FIRST_POS = Y_FIRST_POS+50

turtle.done()
