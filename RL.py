
# coding: utf-8

# Reinforcement Learning
# ====

# Outline
# ---
# ***
# * Introduction & Motivation
#     * What is Reinforcement Learning (RL) ?
#     * Markov Decision Process (MDPs)
#     * Bellman Equations
# * Model-Based Reinforcement Learning
#     * Value Iteration 
#     * Policy Iteration 
# * Model-Free Reinforcement Learning
#     * Monte Carlo Control
#     * SARSA
#     * Q-Learning
# * Discussion, References, Further Reading

# What is Reinforcment Learning? 
# ---
# ***
# * *Reinforcement learning is the study of how animals and artificial systems can learn to optimize their behavior in the face of rewards and punishments* -- Peter Dyan, Encyclopedia of Cognitive Science
# * Not Supervised Learning - the animal/agent is not provided with examples of optimal behaviour, it has to be discovered!
# * It subsumes most Artificial Intelligence problems. Forms the basis of most modern intelligent agents frameworks
# * Ideas drawn from a wide range of contexts, including psychology (e.g, Skinner's "Operant Conditioning") and Philosophy (e.g, "Freedom, Equality, Property and Bentham"), neuroscience, operations research  

# Examples of Reinforcement Learning
# ---
# ***
# * Play Backgammon/Chess/Go/Poker (at human or superhuman level)
# * Hellicopter Control
# * Learn how to walk/crawl/swim/cycle
# * Elevator Scheduling
# * Optimising an petreulem refinery 
# 
# 

# The Markov Decision Process
# ---
# ***
# * The primary abstraction we are going to work in is the Markov Decision Process (MDP). 
# * MDPs capture the dynamics of a mini-world/universe/environment
# * An MDP is defined as a tuple $<S,A,T,R,\gamma>$ where: 
#     * $S$, $s \in S$ is a set of states
#     * $A$, $a \in A$ is a set of actions
#     * $R:S$, $R(s)$ is a function that maps states to rewards
#     * $T:S\times S\times A$, with $T(s'| s, a)$ being the probability of an agent landing from state $s$ to state $s'$ if it takes action $a$
#     * $\gamma$ is a discount factor - the impact of time on rewards
# 

# In[36]:

class MDP:
    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. We also keep track of a gamma value, for use by
    algorithms. We also keep track of the possible states, terminal states, and
    actions for each state. [page 615]"""

    def __init__(self, init, actlist, terminals, gamma=.99):
        update(self, init=init, actlist=actlist, terminals=terminals,
               gamma=gamma, states=set(), reward={})

    def R(self, state):
        "Return a numeric reward for this state."
        return self.reward[state]

    def T(state, action):
        """Transition model.  From a state and an action, return a list
        of (result-state, probability) pairs."""
        abstract
        
    def sample(state, action):
        """Sample from state action. Returns a new state"""
        abstract

    def actions(self, state):
        """Set of actions that can be performed in this state.  By default, a
        fixed list of actions, except for terminal states. Override this
        method if you need to specialize by state."""
        if state in self.terminals:
            return [None]
        else:
            return self.actlist


# The Markov Property and States
# ---
# ***
# * States represent sufficient statistics. 
# * Markov Property ensures that we only care about the present in order to act, not past states
# * Think Tetris - All information are can be captured by a single screenshot
# 
# 1984 Original Version|1986 DOS Version 
# -------------        | -------------
# <img src="250px-Tetris-VeryFirstVersion.png" alt="Drawing" style="width: 300px;">           | <img src="250px-Tetris_DOS_1986.png" alt="Drawing" style="width: 300px;">
# * States $s$ where there are no actions are called *terminal*(e.g., endgames) - there are other definitions as well
# 
# 
# 
# 

# Agents, Actions and Transitions
# ---
# ***
# * An agent is an entity capable of actions
# * An MDP can capture any environment that is inhabited either by exaclty one agent or that other agents are not adaptive
# * Notice how actions are described by the MDP, which captures the world dynamics, not the agent
# * In effect, the agent is just a "brain in a vat", an action-selector
# * The Agent perceives states/rewards and outputs actions
# * Transitions specify the effects of actions in the world (e.g.,  in Tetris, you push a button, the block spings)

# Rewards and the Discount Factor
# ---
# ***
# * Rewards describe state preferences
# * Agent is happier in some states of the MDP (e.g. in Tetris when the block level is low - a fish in water)
# * Punishment is just low/negative reward
# * $\gamma$
#     * the discount factor, describes the impact of time on rewards 
#     * "I want it now", the lower $\gamma$ is the less important future rewards are 
# * There are no "springs of rewards" in the real world - "human nature ?"

# Examples of Reward Schemes
# ---
# ***
# * Scoring in most video games
# * The distance a robot walked for a bipedal robot
# * The amount of food an animal eats
# * Money in modern societies
# * Army Medals ("Gamification") 
# *  (- Fuel spend on a flight)(+ Distance Covered)
# * Cold/Hot 

# Long Term Thinking
# ---
# * It might be better to delay satisfaction
# * Immidiate reward is not allways the maximum reward
# * In some settings there are no immidiate rewards at all (e.g. some solitaire games) 
# * MDPs and RL capture this
# * "Not going out tonight, study"
# * Long term investement

# Policy
# ---
# ***
# * The MDP (the universe) is populated by an Agent (an actor)
# * You can take actions (e.g. move around, move blocks)
# * The type of actions you take under a state is called the *policy*
# * $\pi_\theta: S \times A$, $\pi_\theta(s|a)$, a probabalistic mapping between states and actions, using parameters theta
# * Finding an optimal policy is *mostly* what the RL problem is all about
# 

# The Full Loop
# ---
# ***
# * See how the universe described by the MDP defines actions, not just states and transitions
# * An agent needs to action upon what it perceives
# * Notice the lack of body - "brain in a vat". Body is assumed to be part of the world. 
# 
# <img style="float:centre" src="RL.png">
# 
# 
# 
# 
# 

# Example MDP - EagleWorld
# ---
# ***
# <img style="float:left" src="MDPExample.png">
# 

# Agent Goals
# ---
# ***
# * The agents goal is to maximise its long term reward $J(\theta) = \mathbb{E}_{\pi_{\theta}}\left[\sum\limits_{t=0}^\infty{\gamma^tR(s)}\right]$
# 
# * $\underset{\theta}{\operatorname{argmax}}  J(\theta)$
# * Risk Neutral Agent - think of the EagleWorld Example
# * Rewards can be anything, but most organisms receive rewards only in a very limited amount of states (e.g., fish in water)
# * What if your reward signal is money ?
# * Sociopathic, Egotistic, Greed-is-good Gordon Gecco
# 

# Searching for a Good Policy
# ---
# ***
# * One can possibly search through all combinations of policies until he finds the best
# * Slow, does not work in larger MDPs
# * Exploration/Exploitation Dillema
#     * How much time/effort should be spend exploring for solutions
#     * How much time should be spend exploiting good solutions
# 

# Bellman Expectation Equations
# ---
# ***
# * There are the two most important functions related to an MDP 
# * Recursive definitions
# * $ {V^\pi (s) = R(s) + \sum\limits_{a \in A}\pi(s|a)\left( \gamma\sum\limits_{s' \in S} T(s'|s,a) V^\pi(s')     \right)}$ 
# * ${Q^\pi (s,a) =  \gamma\sum\limits_{s' \in S} T(s'|s,a)R(s')\left(   \sum\limits_{a' \in A}\pi(a',s')Q(s',a')    \right)}$ 
# * Called Q-Value(s) and V-Value(s) respectively
# * They are also interrelated
# * $Q^\pi(s,a) = \sum\limits_{s' \in S} T(s'|s,a) V^\pi(s')$
# * $V^\pi(s) =  \sum\limits_{a' \in A} \pi(s|a) Q^\pi(s,a)$
# 

# Optimal Policy and the Bellman Optimality Equation
# ---
# ***
# * An optimal policy can be defined in terms of Q-values
# * It is the policy that maximises Q values
# * $Q^*(s,a) = \max\limits_\pi Q(s,a)$
# * $Q^*(s,a) = \gamma\sum\limits_{s' \in S} T(s'|s,a)R(s')\max\limits_a'Q(s',a')$
# * $\pi^*(s,a) = \begin{cases} 1, & \mbox{if } \mbox{ $a = \underset{a \in A}{\operatorname{argmax}}  Q^*(s,a)$} \\ 0, & \mbox{if } \mbox{ otherwise} \end{cases}$

# In[37]:

def Q_value(a, s, V, mdp):
    "The expected reward of doing action a in state s, according to the MDP and V."
    return sum([p * V[s_prime] for (p, s_prime) in mdp.T(s, a)])

def optimal_policy(mdp, V):
    """Given an MDP and a value function V, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:Q_value(a, s, V, mdp))
    return pi



# Example MDP - EagleWorld (2)
# ---
# ***
# 
# <img style="float:left" src="MDPExample.png">
# <center><font color='red'>$\pi(Flying, Attack\_Boar) = 1/3, \pi(Flying, Attack\_Turtle) = 1/3, \pi(Flying, Keep\_Flying) = 1/3$</font></center>
# <center><font color='red'>$Q(Flying, Attack\_Boar)   = 0.99 * (10 * 0.5 + 0.5* -1) = 4.455$</font></center>
# <center><font color='red'>$Q(Flying, Attack\_Turtle) = 0.99 * (0.9 * 3 + 0.1* -1) = 2.574$</font></center>
# <center><font color='red'>$Q^\pi(Flying, Keep\_Flying) = 0.99  (0.33  Q^\pi(Flying, Attack\_Turtle) + 0.33  Q(Flying, Attack\_Boar) + 0.33 Q(Flying, Keep\_Flying)$</font></center>

# Example MDP - EagleWorld (2)
# ---
# ***
# 
# <img style="float:left" src="MDPExample.png">
# <center><font color='red'>$Q(Flying, Attack\_Boar)   = 0.99 * (10 * 0.5 + 0.5* -1) = 4.455$</font></center>
# <center><font color='red'>$Q(Flying, Attack\_Turtle) = 0.99 * (0.9 * 3 + 0.1* -1) = 2.574$</font></center>
# <center><font color='red'>$Q^*(Flying, Keep\_Flying) = 0.99  (max ( Q^*(Flying, Attack\_Turtle) , Q(Flying, Attack\_Boar), Q(Flying, Keep\_Flying))$</font></center>
# <center><font color='red'>$\pi(Flying,Attack\_Boar = 1)$</font></center>

# Agents Revisited
# ---
# ***
# * An Agent can be composed of a number of things
#   * A policy 
#   * A Q-Value/and or V-Value Function
#   * A Model of the environment (the MDP)
#   * Inference/Learning Mechanisms
#   * ...
# * An agent has to be able to *create a policy* either on the fly or using Q-Values 
# * The Model/Q/V-Values serve as intermediate points towards construcing a policy

# Relationship to the rest of Machine Learning
# ---
# ***
# * How can one learn a model of the world ? 
#     * Possibly by breaking it down into smaller, abstract chunks
#         * Unsupervised Learning
#     * ... and learning what effects ones actions have the envinroment
#         * Supervised Learning
# * RL weaves all fields of Machine Learning (and possibly Artificial Intelligence) into one coherent whole
# * The purpose of all learning is action!
#     * You need to be able to recognise faces so you can create state
#     * ... and act on it
# 

# *Review Questions*
# ---
# ***
# 1. Give a brief, intuitive description of Reinforcment Learning
# 2. Define a Markov Decision Process
# 2. Define an Agent
# 3. Define the policy of an agent
# 5. What is an Optimal Policy ? 
# 4. Assume an MDP with with single state $s_0$ and two actions $a_0, a_1$. Assume a policy $\pi(s_0|a_0) = 0.3$, $\pi(s_0|a_1) = 0.7$. Briefly give an intuitive explanation of the policy in this setting. 
# 5. Assume an MDP with states $s_0, s_1, s_2$, $R(s_0) = 0$, $R(s_1) = 2$ and $R(s_2) = 1$ and actions $a_0,a_1$. Also assume transitions $T(s_1|s_0, a_0) = 1$, $T(s_2|s_0,a_1) = 1$. State $s_1,s_2$ are terminal  
#     1. What is Q(s_0,a_0) and Q(s_0,a_1) ? 
#     1. What should be the policy $\pi(s_0|a_0)$ and $\pi(s_0|a_1)$ ? 
#     1. What is V(s_0) ? 
# 6. Think of a simple MDP and draw it. Does it have terminal states ? Can it be solved directly using Bellman Backups ? 
# 

# Model Based Reinforcement Learning
# ---
# ***
# * ...also known as planning in certain contexts
# * Who was doing the thinking in the previous example (You? The eagle ?)  
# * An agent has access to model, i.e. has a copy of the MDP (the outside world) in its brain
# * Using that copy, it tries to "think" what is the best route of action
# * It than executes this policy on the real world MDP
# * You can't really copy the world inside your head, but you can copy the dynamics
# * "This and that will happen if I push the chair"
# * Thinking, introspection...

# In[403]:

from utils import *
import matplotlib.pyplot as plt


class GridMDP(MDP):
    """A two-dimensional grid MDP, as in [Figure 17.1].  All you have to do is
    specify the grid as a list of lists of rewards; use None for an obstacle
    (unreachable state).  Also, you should specify the terminal states.
    An action is an (x, y) unit vector; e.g. (1, 0) means move east."""
    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        MDP.__init__(self, init, actlist=orientations,
                     terminals=terminals, gamma=gamma)
        update(self, grid=grid, rows=len(grid), cols=len(grid[0]))
        for x in range(self.rows):
            for y in range(self.cols):
                self.reward[x, y] = grid[x][y]
                if grid[x][y] is not None:
                    self.states.add((x, y))
        self.orig_grid = grid

    def T(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            return [(0.8, self.go(state, action)),
                    (0.1, self.go(state, turn_right(action))),
                    (0.1, self.go(state, turn_left(action)))]

    def go(self, state, direction):
        "Return the state that results from going in this direction."
        state1 = vector_add(state, direction)
        return if_(state1 in self.states, state1, state)

    def to_grid(self, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        grid = []
        for x in range(self.rows):
            line = []
            for y in range(self.cols):
                line += [mapping[x,y]]#
            grid.append(line)
                         
        return grid
              
    def to_arrows(self, policy):
        """Print text arrows from a policy."""
        chars = {(1, 0):'v', (0, 1):'>', (-1, 0):'^', (0, -1):'<', None: '.'}
        return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))
    
    def to_plt_arrows(self,values, policy):
        """Create an image from a values function and a policy ."""
        plt = self.to_plt(self.to_grid(values))
        chars = {(1, 0):(0,0.2), (0, 1):(0.2,0), (-1, 0):(0,-0.2), (0, -1):(-0.2,0), None: None}
        #policy = dict([(s, chars[a]) for (s, a) in policy.items()])
        #print policy
        for x in range(self.rows):
            line = []
            for y in range(self.cols):
                #print x,y,  policy[x,y], "policy"
                val = chars[policy[x,y]]
                if(val is not None):
                    plt.arrow(y,x,val[0],val[1], hold = True)
                
    
    def to_plt(self, grid = None, fig = None):
        """Create an image from a grid, intensity representing reward ."""
        #import numpy as np
        if(grid is None):
            grid = self.grid
        plt.clf()
        # Choose gray colormap
        cmap = plt.get_cmap("gist_gray")
        # Set ticks to the way we like them
        xticks = np.arange(0, len(grid[0]), 1)
        yticks = np.arange(0, len(grid), 1.0)
        plt.xticks(xticks) 
        plt.yticks(yticks)
        extent = np.array([- 0.5,len(grid[0])- 0.5, len(grid) - 0.5, - 0.5]) 
        # create the image
        cax = plt.imshow(grid, cmap = cmap, interpolation="nearest", aspect='equal', extent=extent, origin='upper')
        #cax = plt.imshow(grid, cmap = cmap, interpolation="nearest")

        # Add colorbar
        cbar = plt.colorbar(cax, ticks=[-1, 0, 1])
        #plt.grid(True)
        for tick in xticks[:-1]: plt.axhline(tick + 0.5)
        for tick in yticks: plt.axvline(tick + 0.5)
        plt.hold(True)
        if (fig is not None):
            plt.savefig(fig)
        return plt



# In[404]:

grid = [[-0.04, -0.04, -0.04, +1],
        [-0.04, -0.04, -0.04, -1],
        [-0.04, -0.04, -0.04, -0.04]]
terminals = [(0, 3), (1, 3)]
gmdp = GridMDP(grid,terminals=terminals)


# In[406]:

plt = gmdp.to_plt(fig = "grid.png")
plt.show()


# In[409]:

def value_iteration(mdp, epsilon=0.001):
    "Solving an MDP by value iteration."
    #print mdp.states
    V1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        V = V1.copy() 
        delta = 0
        for s in mdp.states:
            V1[s] = R(s) + gamma * max([sum([p * V[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(V1[s] - V[s]))
        if delta < epsilon * (1 - gamma) / gamma:
             return V


# In[419]:

values = value_iteration(gmdp)
policy =  optimal_policy(gmdp, values)
gmdp.to_plt_arrows(value, policy)


# In[559]:

def policy_iteration(mdp):
    "Solve an MDP by policy iteration [Fig. 17.7]"
    U = dict([(s, 0) for s in mdp.states])
    pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
    while True:
        U1 = U.copy()
        U1 = policy_evaluation(pi, U1, mdp)
        unchanged = True
        #print U1
        for s in mdp.states:   
            a = argmax(mdp.actions(s), lambda a: Q_value(a,s,U1,mdp) + random.random()*0.00000001)
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return U1, pi

def policy_evaluation(pi, U, mdp, k=50):
    """Return an updated utility mapping U from each state in the MDP to its
    utility, using an approximation (modified policy iteration)."""
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(k):
        for s in mdp.states:
            U[s] = R(s) + gamma * sum([p * U[s1] for (p, s1) in T(s, pi[s])])
    return U
    


# In[560]:

gmdp = GridMDP(grid,terminals=terminals)


# In[562]:

values, policy  = policy_iteration(gmdp)
gmdp.to_plt_arrows(values, policy)


# In[561]:




# In[ ]:



