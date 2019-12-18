import random

class card:
    def  __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return str(self.val) + "of" + self.suit

class deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["spades", "hearts", "clubs", "diamond"]:
            for v in range(1, 14):
                self.cards.append(card(s,v))

    def __str__(self):
        ret = ""
        for c in self.cards:
            ret = str(c) + "\n"
        
        return ret

    def shuffle(self):
        for i in range(0, len(self.cards)):
            r = random.randint(0, i)
            # c = self.pop(r)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            # return c

    def draw(self):
        r = random.randint(0, len(self.cards))
        c = self.cards.pop(r)
        return c


d = deck()
d.build()
d.shuffle()
print(d.draw())        

