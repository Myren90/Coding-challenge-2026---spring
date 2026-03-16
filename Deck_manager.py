import turtle
import Data_base
import textwrap

'''
This code handles display of cards using turtle
first code writen and could be cleaned up
'''

t = turtle.Turtle(visible=False)
t.speed(0)

def draw_decks(cooldowns): #draws the 5 main decks and their number and cooldown
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
        t.goto(-370 + (i*200),-150)
        t.color("black")
        t.end_fill()
        t.teleport(-320 + (i*200),-145)
        t.write(i+1,align="center",font=("Arial",15,"bold"))
        t.color("blue")
        t.teleport(t.teleport(-320 + (i*200),-200))
        t.write(cooldowns[i],align="center",font=("Arial",20,"bold"))
    t.pendown()
    turtle.update()


def write_multilined_text(t,text, start_pos=(0, 0), max_width=40, line_height=30, font=("Arial", 16, "normal")): #draws card on text, this is code I had to get help with
    wrapped_lines = textwrap.wrap(text, width=max_width)

    t.penup()
    t.goto(start_pos)
    t.pendown()
    

    for i, line in enumerate(wrapped_lines):
        t.write(line, align="left", font=font)
        
        t.penup()
        t.goto(start_pos[0], start_pos[1] - (i + 1) * line_height)
        t.pendown()
    turtle.update()

def draw_card_in_decks(deck_num,color="lightgrey"): #draws cards of selected decks
    t.clear()
    t.pendown()
    t.pensize(5)
    t.teleport(-300, - 200)
    for i in range(5):
        if deck_num[i] != -1:
            t.color(color)
            t.teleport(-370 + (i*200),-130)
            t.begin_fill()
            t.goto(-370+150 + (i*200),-130)
            t.goto(-370 + 150+ (i*200),-200 - 200)
            t.goto(-370+ (i*200),-200 - 200)
            t.goto(-370 + (i*200),-130)
            t.color("grey")
            t.end_fill()
    t.pendown()
    t.color("Black")
    g = 0
    for i in deck_num: #draws the text on the cards from data base
        if i != -1:
            t.teleport(-300 + (g*200),-145)
            t.write(g+1,font=("Arial",15,"bold"))
            t.teleport(-360 + (g*200),-170)
            card_text = Data_base.get_card_info(i)
            write_multilined_text(t,card_text,(t.xcor(),t.ycor()),20,15,("Arial",10,"normal"))
        g += 1
    turtle.update()

def clear_decks(): #removes the decks from the screen
    t.clear()