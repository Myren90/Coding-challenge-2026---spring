import turtle
import keyboard
import grid_turtle_code

"""
player code, handles player health and will manage several different parts
"""
            

def setup_player(t,player_id):
    t.shape("circle")
    t.color("blue")
    grid_turtle_code.goto_grid(t,10,10, player_id)
    t.penup()
    