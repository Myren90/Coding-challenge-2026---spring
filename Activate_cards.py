import turtle
import keyboard
import grid_turtle_code
import copy
#from Main import attack_list
'''
this code is the code that actully plays cards
'''
attack_list = []
damage = 0
conditions = ""

def add_to_attack_list(player_id,x,y):
    attack_list.append((player_id[0] + x, player_id[1] + y))

def get_data():
    global damage
    return attack_list, damage,conditions


def play_card(id,t,player_id,terrain):
    global damage
    damage = 0
    block_terrian = copy.deepcopy(terrain)
    current_pos = player_id[:]
    
    if id == 1:
        grid_turtle_code.highlight_squares(type="cross", size=1,start_posistion=current_pos,include_keys=True,blocked_terrian=block_terrian)
        while True:
            if keyboard.is_pressed("w"):
                current_pos = grid_turtle_code.move_grid(t,0,1,current_pos,block_terrian)
                break
            if keyboard.is_pressed("s"):
                current_pos = grid_turtle_code.move_grid(t,0,-1,current_pos,block_terrian)
                break
            if keyboard.is_pressed("a"):
                current_pos = grid_turtle_code.move_grid(t,-1,0,current_pos,block_terrian)
                break
            if keyboard.is_pressed("d"):
                current_pos = grid_turtle_code.move_grid(t,1,0,current_pos,block_terrian)
                break
        grid_turtle_code.clear_highlingting()
    elif id == 2:
        grid_turtle_code.highlight_squares(type="star", size=1,start_posistion=current_pos,include_keys=True,blocked_terrian=block_terrian)
        while True:
            if keyboard.is_pressed("w"):
                current_pos = grid_turtle_code.move_grid(t,1,1,current_pos,block_terrian)
                break
            if keyboard.is_pressed("a"):
                current_pos = grid_turtle_code.move_grid(t,1,-1,current_pos,block_terrian)
                break
            if keyboard.is_pressed("s"):
                current_pos = grid_turtle_code.move_grid(t,-1,-1,current_pos,block_terrian)
                break
            if keyboard.is_pressed("d"):
                current_pos = grid_turtle_code.move_grid(t,-1,1,current_pos,block_terrian)
                break
        grid_turtle_code.clear_highlingting()
    elif id == 3:
        damage += 3
        grid_turtle_code.highlight_squares(type="cross", size=3,start_posistion=current_pos,include_keys=True,blocked_terrian=block_terrian)
        while True:
            if keyboard.is_pressed("w"):
                for i in range(3):
                    #attack_list.append((player_id[0],player_id[1] + i + 1))
                    add_to_attack_list(player_id,0,i+1)
                break
            if keyboard.is_pressed("a"):
                for i in range(3):
                    #attack_list.append((player_id[0] - i - 1,player_id[1]))
                    add_to_attack_list(player_id,-i-1,0)
                break
            if keyboard.is_pressed("s"):
                for i in range(3):
                    #attack_list.append((player_id[0],player_id[1] - i - 1))
                    add_to_attack_list(player_id,0,-i-1)
                break
            if keyboard.is_pressed("d"):
                for i in range(3):
                    #attack_list.append((player_id[0] + i + 1,player_id[1]))
                    add_to_attack_list(player_id,i+1, 0)
                break
        grid_turtle_code.clear_highlingting()
    elif id == 4:
        damage += 5
        add_to_attack_list(player_id,0,1)
        add_to_attack_list(player_id,0,-1)
        add_to_attack_list(player_id,1,0)
        add_to_attack_list(player_id,-1,0)
        add_to_attack_list(player_id,1,1)
        add_to_attack_list(player_id,-1,1)
        add_to_attack_list(player_id,1,-1)
        add_to_attack_list(player_id,-1,-1)


    return current_pos