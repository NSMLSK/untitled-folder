import random


cards = []
suits = [ "spades" , "clubs", "hearts" , "diamonds"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
def shuffle():
    card = cards.pop()
    return card

def deal():
    card = cards.pop()
    return card

shuffle()
card = deal()

print(card)




