import turtle
import keyboard
import grid_turtle_code

'''
this code is the code that actully plays cards
'''
def play_card(id,t,player_id,block_terrian):
    if id == 1:
        grid_turtle_code.highlight_squares(type="cross", size=1,start_posistion=player_id,include_keys=True)
        while True:
            if keyboard.is_pressed("w"):
                player_id = grid_turtle_code.move_grid(t,0,1,player_id)
                break
            if keyboard.is_pressed("s"):
                player_id = grid_turtle_code.move_grid(t,0,-1,player_id)
                break
            if keyboard.is_pressed("a"):
                player_id = grid_turtle_code.move_grid(t,-1,0,player_id)
                break
            if keyboard.is_pressed("d"):
                player_id = grid_turtle_code.move_grid(t,1,0,player_id)
                break
        grid_turtle_code.clear_highlingting()
    elif id == 2:
        grid_turtle_code.highlight_squares(type="star", size=1,start_posistion=player_id,include_keys=True)
        while True:
            if keyboard.is_pressed("w"):
                player_id = grid_turtle_code.move_grid(t,1,1,player_id)
                break
            if keyboard.is_pressed("a"):
                player_id = grid_turtle_code.move_grid(t,1,-1,player_id)
                break
            if keyboard.is_pressed("s"):
                player_id = grid_turtle_code.move_grid(t,-1,-1,player_id)
                break
            if keyboard.is_pressed("d"):
                player_id = grid_turtle_code.move_grid(t,-1,1,player_id)
                break
        grid_turtle_code.clear_highlingting()