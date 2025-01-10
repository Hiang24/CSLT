from Bai118 import createDeck,shuffle

def deal():
    hand = int(input("Number of hands: "))
    list_hand= [[] for _ in range(hand)]
    card_per_hand = int(input("Number of cards per hand: "))
    deck_of_card = shuffle(createDeck())
    return list_hand,card_per_hand,deck_of_card

def dealing_the_hands(list_hand,card_per_hand,deck):
    while len(list_hand[-1])<card_per_hand:
        for hand in list_hand:
            hand.append(deck.pop(0))
    return list_hand
def inkq(after_deal):
    for i in range(len(after_deal)):
        print("Hand {}:".format(i+1),after_deal[i])
        
list_hand,cards,deck = deal()
after_deal = dealing_the_hands(list_hand,cards,deck)
inkq(after_deal)