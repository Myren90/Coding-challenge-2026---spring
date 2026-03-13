import keyboard
import Deck_manager
import Activate_cards

def card_player(player_deck_1, player_deck_2, player_deck_3, player_deck_4, player_deck_5,deck_selected):
    if keyboard.is_pressed("space"):
        return "reset"
    if deck_selected == 1:
            if keyboard.is_pressed("1"):
                Activate_cards.play_card(player_deck_1[0])
                return "false"
            elif keyboard.is_pressed("2"):
                Activate_cards.play_card(player_deck_1[1])
                return "false"
            elif keyboard.is_pressed("3"):
                Activate_cards.play_card(player_deck_1[2])
                return "false"
            elif keyboard.is_pressed("4"):
                Activate_cards.play_card(player_deck_1[3])
                return "false"
            elif keyboard.is_pressed("5"):
                Activate_cards.play_card(player_deck_1[4])
                return "false"
            else:
                return "true"
    elif deck_selected == 2:
            if keyboard.is_pressed("1"):
                Activate_cards.play_card(player_deck_2[0])
                return "false"
            elif keyboard.is_pressed("2"):
                Activate_cards.play_card(player_deck_2[1])
                return "false"
            elif keyboard.is_pressed("3"):
                Activate_cards.play_card(player_deck_2[2])
                return "false"
            elif keyboard.is_pressed("4"):
                Activate_cards.play_card(player_deck_2[3])
                return "false"
            elif keyboard.is_pressed("5"):
                Activate_cards.play_card(player_deck_2[4])
                return "false"
            else:
                return "true"
    elif deck_selected == 3:
            if keyboard.is_pressed("1"):
                Activate_cards.play_card(player_deck_3[0])
                return "false"
            elif keyboard.is_pressed("2"):
                Activate_cards.play_card(player_deck_3[1])
                return "false"
            elif keyboard.is_pressed("3"):
                Activate_cards.play_card(player_deck_3[2])
                return "false"
            elif keyboard.is_pressed("4"):
                Activate_cards.play_card(player_deck_3[3])
                return "false"
            elif keyboard.is_pressed("5"):
                Activate_cards.play_card(player_deck_3[4])
                return "false"
            else:
                return "true"
    elif deck_selected == 4:
            if keyboard.is_pressed("1"):
                Activate_cards.play_card(player_deck_4[0])
                return "false"
            elif keyboard.is_pressed("2"):
                Activate_cards.play_card(player_deck_4[1])
                return "false"
            elif keyboard.is_pressed("3"):
                Activate_cards.play_card(player_deck_4[2])
                return "false"
            elif keyboard.is_pressed("4"):
                Activate_cards.play_card(player_deck_4[3])
                return "false"
            elif keyboard.is_pressed("5"):
                Activate_cards.play_card(player_deck_4[4])
                return "false"
            else:
                return "true"
    elif deck_selected == 5:
            if keyboard.is_pressed("1"):
                Activate_cards.play_card(player_deck_5[0])
                return "false"
            elif keyboard.is_pressed("2"):
                Activate_cards.play_card(player_deck_5[1])
                return "false"
            elif keyboard.is_pressed("3"):
                Activate_cards.play_card(player_deck_5[2])
                return "false"
            elif keyboard.is_pressed("4"):
                Activate_cards.play_card(player_deck_5[3])
                return "false"
            elif keyboard.is_pressed("5"):
                Activate_cards.play_card(player_deck_5[4])
                return "false"
            else:
                return "true"


def card_menue(player_deck_1, player_deck_2, player_deck_3, player_deck_4, player_deck_5):
    deck_selected = 0
    sentry = "true"
    Deck_manager.draw_decks()
    while sentry == "true":
        if deck_selected == 0:
            if keyboard.is_pressed("1"):
                Deck_manager.draw_card_in_decks(player_deck_1)
                deck_selected = 1
            elif keyboard.is_pressed("2"):
                Deck_manager.draw_card_in_decks(player_deck_2)
                deck_selected = 2
            elif keyboard.is_pressed("3"):
                Deck_manager.draw_card_in_decks(player_deck_3)
                deck_selected = 3
            elif keyboard.is_pressed("4"):
                deck_selected = 4
                Deck_manager.draw_card_in_decks(player_deck_4)
            elif keyboard.is_pressed("5"):
                deck_selected = 5
                Deck_manager.draw_card_in_decks(player_deck_5)
            else:
                deck_selected = 0
        else:
            sentry = card_player(player_deck_1, player_deck_2, player_deck_3, player_deck_4, player_deck_5,deck_selected)
            if sentry == "reset":
                deck_selected = 0
                Deck_manager.draw_decks()
                sentry = "true"

            
        if keyboard.is_pressed("escape"):
            sentry = False
    print("Card selected")
