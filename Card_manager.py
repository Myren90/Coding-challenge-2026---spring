import keyboard
import Deck_manager
import Activate_cards
import time
import Card_manager

'''
This scrip handles the card playing code
'''

def card_player(current_hand,player,player_id,blocked_terrian,cooldown,active_deck): #this is the code to play a card after getting the active deck
        for i in range(5):
            if keyboard.is_pressed(str(i+1)) and current_hand[i] != -1:
                player_id = Activate_cards.play_card(current_hand[i],player,player_id,blocked_terrian)
                current_hand[i] = -1
                Deck_manager.draw_card_in_decks(current_hand,"green")
        if all(i == -1 for i in current_hand): #adds cooldown to played deck
            cooldown[active_deck-1] += 2
            return False,player_id
        else:
            return True,player_id
            
        
def card_menue(decks,player,player_id,blocked_terrian,cooldowns): # this is where the player chooses a deck
    deck_selected = 0
    active_deck = 0
    current_hand = []
    sentry = True
    Deck_manager.draw_decks(cooldowns)
    while sentry:
        if deck_selected == 0:
            for i in range(5): #preview/select decks
                key = str(i + 1)
                if keyboard.is_pressed(key):
                    active_deck = i + 1
                    if cooldowns[i] > 0:
                        Deck_manager.draw_card_in_decks(decks[i],"red")
                    else:
                        Deck_manager.draw_card_in_decks(decks[i])
                    current_hand = decks[i][:]
                    break
            if keyboard.is_pressed("space"): #go back to main deck view
                active_deck = 0
                Deck_manager.draw_decks(cooldowns)
                current_hand = []

        if active_deck != 0 and keyboard.is_pressed("enter") and cooldowns[active_deck-1] < 1: #confirm active deck
            deck_selected = active_deck
            Deck_manager.draw_card_in_decks(current_hand,"green")

        if deck_selected != 0: #moves to playing card function
            sentry,player_id = card_player(current_hand,player,player_id,blocked_terrian,cooldowns,deck_selected)

        if keyboard.is_pressed("9"): #infinite loops stopper for debuging
            sentry = False
    return player_id
