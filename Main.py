import grid_turtle_code
import turtle
import player_controller
import Deck_manager
import keyboard
import Card_manager

sentry = True

t = turtle.Turtle()
win = turtle.Screen()

player_deck_1 = [0,1,2,3,4]
player_deck_2 = [5,6,7,8,9]
player_deck_3 = [10,11,12,13,14]
player_deck_4 = [15,16,17,18,19]
player_deck_5 = [20,21,22,23,24]

win.setup(height=700,width=1200)
grid_turtle_code.draw_grid(t,30,16,32,-380,330)
player_controller.setup_player()

Card_manager.card_menue(player_deck_1,player_deck_2,player_deck_3,player_deck_4,player_deck_5)



