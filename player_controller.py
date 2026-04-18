import turtle
import keyboard
import grid_turtle_code

"""
player code, handles player health and will manage several different parts
"""
health = 100
health_bar = turtle.Turtle(visible=False)

def setup_player(t,player_id):
    t.shape("circle")
    t.color("blue")
    grid_turtle_code.goto_grid(t,1,1, player_id)
    t.penup()
    player_health(0)
    return player_id

def player_health(damage):
    health_bar.clear()
    global health
    health -= damage
    health_bar.color("green")
    health_bar.teleport(-400,0)
    health_bar.begin_fill()
    health_bar.goto(-420,0)
    health_bar.goto(-420,health*2)
    health_bar.goto(-400,health*2)
    health_bar.goto(-400,0)
    health_bar.end_fill()
    turtle.update()


    