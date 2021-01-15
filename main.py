# Build a deck

class Symbol:
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def __str__(self):
        return "{} {}".format(self.color, self.icon)


class Card(Symbol):
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    #def __str__(self):
        #return "{} of {}".format(self.value, self.Symbol)

    # 1st version i tried out
    def show(self):
        print("The {} {} of {}".format(self.value, self.color, self.icon))



class Deck :
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for k in ["Red", "Black"] :
            if k == "Red" :
                for s in ["(U+2665)", "(U+2666)"] :  # Hearts , Diamonds, Clubs, Spades
                    for v in range(1, 14):
                        self.cards.append(Card(k, s, v))
            else :
                for s in ["(U+2663)", "(U+2660)"] :
                    for v in range(1, 14):
                        self.cards.append(Card(k, s, v))

    def show(self):
        for c in self.cards:
            c.show()

    #def __str__(self):
        #for c in self.cards :
            #print(Deck())

deck = Deck()
deck.show()





class Player:
    def __init__(self):
        pass


