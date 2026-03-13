import turtle
import grid_turtle_code

def setup_player():
    player_id = [0,0]
    t = turtle.Turtle()
    t.shape("circle")
    t.color("blue")
    player_id = grid_turtle_code.goto_grid(t,10,10, player_id)
    t.penup()
    player_id = grid_turtle_code.move_grid(t,5,5, player_id)
    print(player_id)