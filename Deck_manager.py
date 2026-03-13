import turtle
import Data_base

t = turtle.Turtle(visible=False)
t.speed(0)

def draw_decks():
    t.clear()
    t.pendown()
    t.pensize(3)
    t.teleport(-300, - 200)
    for i in range(5):
        t.color("grey")
        t.teleport(-370 + (i*200),-150)
        t.begin_fill()
        t.goto(-370+100 + (i*200),-150)
        t.goto(-370 + 100+ (i*200),-200 - 100)
        t.goto(-370+ (i*200),-200 - 100)
        t.color("black")
        t.end_fill()
    t.pendown()

def draw_card_text(id=0):
    t.color("black")
    t.teleport(-590,300)
    t.write("test",font=("ROG fonts", 10, "normal"))

def draw_card_large(id=0):
    t.teleport(-590,330)
    t.pendown()
    t.pensize(5)
    t.color("darkgrey")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.right(90)
        t.forward(500)
        t.right(90)
    t.color("lightgrey")   
    t.end_fill()
    draw_card_text(t,id)

def draw_card_in_decks(deck_num):
    t.clear()
    t.pendown()
    t.pensize(5)
    t.teleport(-300, - 200)
    for i in range(5):
        t.color("darkgrey")
        t.teleport(-370 + (i*200),-130)
        t.begin_fill()
        t.goto(-370+150 + (i*200),-130)
        t.goto(-370 + 150+ (i*200),-200 - 200)
        t.goto(-370+ (i*200),-200 - 200)
        t.color("grey")
        t.end_fill()
    t.pendown()
    t.color("Black")
    g = 0
    for i in deck_num:
        t.teleport(-370 + (g*200),-200)
        card_text = Data_base.get_card_info(i)
        t.write(card_text,font=("Arial",10,"normal"))
        g += 1

def clear_decks():
    t.clear()