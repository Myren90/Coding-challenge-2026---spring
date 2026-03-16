import grid_turtle_code
import turtle
import player_controller
import Deck_manager
import keyboard
import Card_manager

#defines varibles
sentry = True

t = turtle.Turtle()
win = turtle.Screen()

turtle.tracer(0)

player_deck_1 = [1,1,2,2,3]
player_deck_2 = [5,6,7,8,9]
player_deck_3 = [10,11,12,13,14]
player_deck_4 = [15,16,17,18,19]
player_deck_5 = [20,21,22,23,24]
decks = [player_deck_1, player_deck_2, player_deck_3, player_deck_4, player_deck_5]
player_deck_1_recharge = 0
player_deck_2_recharge = 0
player_deck_3_recharge = 0
player_deck_4_recharge = 0
player_deck_5_recharge = 0
cooldowns = [player_deck_1_recharge,player_deck_2_recharge,player_deck_3_recharge,player_deck_4_recharge,player_deck_5_recharge]

blocked_terrian = []
player_id = [10,10]
player = turtle.Turtle()

#creates screen and creates main game grid and places player icon on grid
win.setup(height=700,width=1200)
grid_turtle_code.draw_grid(t,30,16,32,-380,330)
player_controller.setup_player(player,player_id)

#main game loop
while True:
    if keyboard.is_pressed("space"):
        Card_manager.card_menue(decks,player,player_id,blocked_terrian,cooldowns)
        for i in range(len(cooldowns)):
            if cooldowns[i] > 0:
                cooldowns[i] -= 1
    elif keyboard.is_pressed("escape"):
        break
    

print("Game end")


