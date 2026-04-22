import grid_turtle_code
import turtle
import player_controller
import Deck_manager
import keyboard
import Card_manager
import Enemy
import time
import Activate_cards
print("------------------")
def clean_data(data):
    if not all_unique(data):
        data = make_unique(data)
    return data

def make_unique(lst):

    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list


def all_unique(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    return len(lst) == len(set(lst))

#defines varibles
sentry = True

t = turtle.Turtle()
win = turtle.Screen()

turtle.tracer(0)

player_deck_1 = [1,1,2,2,3]
player_deck_2 = [4,4,2,2,2]
player_deck_3 = [1,1,1,1,1]
player_deck_4 = [2,2,3,3,3]
player_deck_5 = [5,5,5,5,5]
decks = [player_deck_1, player_deck_2, player_deck_3, player_deck_4, player_deck_5]
player_deck_1_recharge = 0
player_deck_2_recharge = 0
player_deck_3_recharge = 0
player_deck_4_recharge = 0
player_deck_5_recharge = 0
cooldowns = [player_deck_1_recharge,player_deck_2_recharge,player_deck_3_recharge,player_deck_4_recharge,player_deck_5_recharge]

blocked_terrian = []

player = turtle.Turtle()
player_id = [0,0]
#creates screen and creates main game grid and places player icon on grid
win.setup(height=700,width=1200)
blocked_terrian = grid_turtle_code.draw_grid(t,30,16,32,-380,330,20)
player_id = player_controller.setup_player(player,player_id)

for i in range(16):
    for j in range(6):
        blocked_terrian.append([-j,i])
        blocked_terrian.append([j+33,i])
for i in range(44):
    for j in range(6):
        blocked_terrian.append([i-5,-j])
        blocked_terrian.append([i-5,j+16])


enemy1 = Enemy.enemy_class(blocked_terrian)
enemy2 = Enemy.enemy_class(blocked_terrian)
enemy3 = Enemy.enemy_class(blocked_terrian)
enemies_on_board = [enemy1,enemy2,enemy3]
#main game loop
while sentry:
    Deck_manager.draw_explainer()
    while True:
        if keyboard.is_pressed("Space"):
            break
        elif keyboard.is_pressed("escape"):
            sentry = False
            break
        elif keyboard.is_pressed("h"):
            Deck_manager.change_state()
            Deck_manager.draw_explainer()
            time.sleep(0.5)
    if sentry == False:
        break
    player_id = Card_manager.card_menue(decks,player,player_id,blocked_terrian,cooldowns)
    attack_list,damage,conditions = Activate_cards.get_data()
    Activate_cards.reset()
    clean_data(attack_list)
    for i in enemies_on_board:
        time.sleep(.25)
        i.take_damage(attack_list,damage)
        i.activate(player_id)
        i.display_health()
    attack_list.clear()
    for i in range(len(cooldowns)):
        if cooldowns[i] > 0:
            cooldowns[i] -= 1

    sentry = player_controller.get_data()
    
    

print("Game end")



# fix emeys spawning on terrain or on player/near player
# game end
#TODO (not able) quite
# dispay which deck you have open
#TODO (not able) Diagram of card ability 
# enemy variance
# help button
#TODO deck building element
