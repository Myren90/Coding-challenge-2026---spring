'''
since this game is going to have alot of card text this code is just a data base of card text. I am sure their is some python way to do this better
'''

def get_card_info(id):
    if id == 0:
        return "This is a test card. Its purpose is to see if this the card texted system works and if any changes need to be made"
    elif id == 1:
        return "------Sprint------- When you play this card, move one space in any horizontal/vertical direction"
    elif id == 2:
        return "--------Dash--------When you play this card move one space in any diagonal direction  "
    elif id == 3:
        return "--------Rife--------When played choose a vertical or horizontal direction, all enemies in that direction take 3 damage"
    elif id == 4:
        return "----Sword Swing----When played all adjacent enimes take 5 damage"
    else:
        return "Null"