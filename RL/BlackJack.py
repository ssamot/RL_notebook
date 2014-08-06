import random




class SimpleBlackJack:
    """A simplified black jack game, similiar to the one in Chapter 5.3 of Sutton and Barto.
    We have two main differences. The deck of cards used is finite (the standard French 52 card deck)
    and all aces count as 11.
    """

    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []
        self.deal()



    def sum(self, cards):
        """ Sum cards in the Black Jack Fashion, except that Aces are always 11"""
        total = 0
        for card in cards:
            if( card[0] == "T" or
                card[0] == "J" or
                card[0] == "Q" or
                card[0] == "K" ):
                val = 10

            elif( card[0] == "A"):
                val = 11

            else:
                val = int(card[0])

            total+=val
        return total


    def deal(self):
        """ Shuffle the deck and restart the game"""
        colour = ["H", "C", "S", "D"]
        number = [str(i) for i in range(2,10)] + ["T", "J", "Q", "K", "A"]
        deck = []
        for c in colour:
            for n in number:
                deck += [n + c]
        random.shuffle(deck)
        self.deck = deck
        self.game_finished = False
        self.player_cards = [self.deck.pop(), self.deck.pop()]
        self.dealer_cards = [self.deck.pop(), self.deck.pop()]

        sum_player = self.sum(self.dealer_cards)
        sum_dealer = self.sum(self.player_cards)

        if(sum_player == 21 and sum_dealer == 21):
            self.game_finished == True
            return 0.0
        if(sum_player == 21 and sum_dealer < 21):
            self.game_finished == True
            return 1.0

    def stick(self):
        """Stop drawing new cards and let the dealer do it"""
        self.game_finished = True

        sum_player = self.sum(self.dealer_cards)
        sum_dealer = self.sum(self.player_cards)

        if(self.game_finished):
            while(sum_dealer < 17 ):
                self.dealer_cards +=[self.deck.pop()]
                sum_dealer = self.sum(self.player_cards)

        if(sum_player > sum_dealer or sum_dealer > 21):
            return 1.0
        if(sum_player == sum_dealer):
            return 0.0
        if(sum_player < sum_dealer):
            return -1.0

    def hit(self):
        """Get a new card from the deck """
        self.player_cards +=[self.deck.pop()]
        sum_player = self.sum(self.dealer_cards)
        if(sum_player > 21):
            self.game_finished = True
            return -1.0
        else:
            return 0.0

    def getState(self):
        """The state (i.e. sum of all cards at hand) """
        return [sum(self.player_cards)]

    def simulate(self, action):
        """Simulate a game in an iterative fashion. Start state is [] """
        if(action == "deal"):
            return self.getState(),  ["stick, hit"], 0 , False


        if(action == "stick"):
            R = self.stick()

        if(action == "hit"):
            R = self.hit()

        if(self.game_finished == True):
            return  [], ["deal"], 0, True
        else:
            return self.getState(),  ["stick, hit"], R , False







