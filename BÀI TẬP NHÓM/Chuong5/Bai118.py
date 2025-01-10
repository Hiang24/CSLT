import random

def createDeck():
    cards=[]
    for ki_tu in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
        for chat in ['s','h','d','c']:
            cards.append(ki_tu + chat)
    return cards

def shuffle(cards):
    new_cards=[]
    while len(cards) > 0:
        i=random.randint(0,len(cards)-1) #chọn ra một số chỉ mục i bất kì trong list cards
        new_cards.append(cards.pop(i)) #thêm vào list new_cards kí tự có số chỉ mục là i trong list cards đồng thời xóa nó trong list card bằng lệnh pop
    return new_cards

if __name__=='__main__':
    cards = createDeck()
    new_cards = shuffle(cards)
    print('Bo bai ban dau:',createDeck())
    print('Bo bai da xao tron:',shuffle(new_cards))