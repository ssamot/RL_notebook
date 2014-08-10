import random
import utils




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
        colour = ["h", "c", "s", "d"]
        number = [str(i) for i in range(2,10)] + ["T", "J", "Q", "K", "A"]
        deck = []
        for c in colour:
            for n in number:
                deck += [n + c]
        random.shuffle(deck)
        self.deck = deck
        self.reached_terminal = False
        self.player_cards = [self.deck.pop(), self.deck.pop()]
        self.dealer_cards = [self.deck.pop(), self.deck.pop()]

        sum_player = self.sum(self.dealer_cards)
        sum_dealer = self.sum(self.player_cards)

        if(sum_player >= 21 and sum_dealer == sum_player):
            self.reached_terminal == True
            return 0.0
        if(sum_player >= 21 and sum_dealer < sum_player):
            self.reached_terminal == True
            return 1.0

        if(sum_dealer >= 21 and sum_dealer > sum_player):
            self.reached_terminal == True
            return -1.0

        if(sum_dealer >= 21 or sum_player >=21):
            assert(False)
        return 0.0

    def stick(self):
        """Stop drawing new cards and let the dealer do it"""
        self.reached_terminal = True

        sum_player = self.sum(self.player_cards)
        sum_dealer = self.sum(self.dealer_cards)

        while(sum_dealer < 17 and sum_dealer < sum_player):
            self.dealer_cards +=[self.deck.pop()]
            sum_dealer = self.sum(self.dealer_cards)


        if(sum_dealer > 21):
            return 1.0
        if(sum_player > sum_dealer):
            return 1.0
        if(sum_player == sum_dealer):
            return 0.0
        if(sum_player < sum_dealer):
            return -1.0

    def hit(self):
        """Get a new card from the deck """
        self.player_cards +=[self.deck.pop()]
        sum_player = self.sum(self.player_cards)
        if(sum_player > 21):
            self.reached_terminal = True
            return -1.0
        else:
            return 0.0

    def getState(self):
        """The state (i.e. sum of all cards at hand) """
        return [self.sum(self.player_cards)]

    def simulate(self, agent, episodes, episodic = True):
        """Simulate a game in an iterative fashion. Start state is [] """

        for i in range(episodes):
            visited_states = []
            actions = []
            rewards = []
            possible_actions = ["deal"]
            previous_state = None
            previous_action = None
            while(not self.reached_terminal):

                state =  self.getState()
                #print possible_actions
                action = agent.selectAction(state, possible_actions)

                assert(state[0] <= 22)

                if(action == "deal"):
                    R = self.deal()

                if(action == "stick"):
                    R = self.stick()

                if(action == "hit"):
                    R = self.hit()

                if( action !="deal"):
                    if(episodic):
                        visited_states.append(state)
                        actions.append(action)
                        rewards.append(R)
                    else:
                        if(previous_action!= "deal"):
                            agent.SARSA(previous_state, previous_action, state, action, R)

                    #if(state[0] == 22 and action == "hit"):
                    #      print visited_states, actions, self.sum(self.player_cards), self.reached_terminal, rewards, self.sum(self.dealer_cards)
                possible_actions = ["stick", "hit"]
                previous_state = state
                previous_action = action

            if(episodic):
                #print visited_states, actions
                agent.MC(visited_states,actions,rewards)
            if(previous_action!= "deal"):
                agent.SARSA(previous_state, previous_action, None, action, R)
            self.player_cards = []
            self.dealer_cards = []
            self.reached_terminal = False





class RLAgent():
    """The top class of all RL agents .
    """
    def __init__(self,learning_rate = 0.01, epsilon = 0.01):
        self.Q = {}
        self.learning_rate = learning_rate
        self.epsilon = epsilon

    def MC(self,visited_states, actions, rewards):
        """" Monte Carlo Control """
        v_t = sum(rewards)

        for i in range(len(visited_states)):
            state = visited_states[i]
            action = actions[i]
            #if(state[0] == 4 and action == "stick"):
            #    print state, action, visited_states,actions, rewards
            state_action, Q = self.__Q(state, action)
            self.Q[state_action]+= self.learning_rate*(v_t - self.Q[state_action] )

    def SARSA(self, previous_state, previous_action, state, action, next_reward):
        """" SARSA(0) """
        if(state is None):
            Q = 0
        else:
            state_action, Q = self.__Q(state, action)
        previous_state_action, previous_Q = self.__Q(previous_state, previous_action)
        #self.Q[state_action]+= self.learning_rate*(reward + previous_Q - self.Q[state_action] )
        self.Q[previous_state_action]+= self.learning_rate*(next_reward + Q - self.Q[previous_state_action]  )


    def selectAction(self, state, actions):
        """ Select an action given a state and a vector of possible actions"""
        r = random.random()
        if(len(actions) == 1):
            return actions[0]
        if(r < self.epsilon):
            return random.choice(actions)
        else:

            return utils.argmax(actions, lambda action: self.__Q(state,action)[1])

    def __Q(self,state, action):
        if(state is None or action is None):
            return 0
        state_action = tuple(state + [action])

        if(state_action not in self.Q):
            self.Q[state_action] = 0

        return state_action, self.Q[state_action]





if __name__=="__main__":
    blackjack = SimpleBlackJack()
    agent = RLAgent(learning_rate=0.01, epsilon=0.01)
    blackjack.simulate(agent,200000,episodic=False)

    from visualisation import Visualiser
    vis = Visualiser()
    vis.Q(agent.Q, fig = "test.png")
    #print agent.Q









