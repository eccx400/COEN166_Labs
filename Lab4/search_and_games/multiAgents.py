# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
	foodArr = newFood.asList()

	curPos = currentGameState.getGhostPosition(1)	
	manDis = util.manhattanDistance(curPos, newPos)

	score = manDis + successorGameState.getScore()
	limit = 99999

	if successorGameState.isWin():
		return float("inf") - 20

	for x in foodArr:
		dots = util.manhattanDistance(x, newPos)
		if( dots < limit):
			limit = dots
			lefood = foodPos
	 
	if newPos in currentGameState.getCapsules():
		score = score + 100

	if manDis <= 2 && newScaredTimes [0] == 0:
		score = -99999
	else
		score = score + 200
        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent & AlphaBetaPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 7)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 8)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.

	The correct implementation of minimax will lead to Pacman winning the game in some tests, but
	it will also lead to Pacman losing the game in some tests.
		• The evaluation function for the pacman test in this part is already written
	(self.evaluationFunction). You shouldn't change this function, but recognize that now we have
	“Look-ahead” agents that evaluate future states whereas reflex agents evaluate actions from the
	current state.
		• Pacman is always agent 0, and the agents move in order of increasing agent index.
		• All states in minimax should be GameStates, either passed in to getAction or generated via
	GameState.generateSuccessor.
        """
        "*** YOUR CODE HERE ***"
	for legal in gameState.getLegalActions():
		if legal != Directions.STOP:
			nextLevel = gameState.generateSuccessor(0, legal)
			score = max(score, getMin(nextLevel, self.depth, 1))

			older = score
		if score > older:
			gameState.getLegalActions() = legal

		else:
			gameState.getLegalActions().remove(Directions.STOP)

		return score

  	
   	ghost = gameState.getNumAgents() - 1
	if(state.isWin() or state.isLose() or depth == 0):
		return self.evaluationFunction(state)
   
	def getMax(self, state, depth)
   		score = float("-inf")

   		for nextLev in state.getLegalActions(0):
			score = max(score, getMin(state.generateSuccessor(0, nextLev), depth - 1, 1))

		return score
   
   	def getMin(self, state, depth, agentNum)
		score = float("inf")
	
		if agentNum == ghost:
			for legal in state.getLegalActions(agentNum):
				score = min(score, getMax(state.generateSuccessor(agentNum, legal), depth - 1))
			else:
				score = min(score, getMin(state.generateSuccessor(agentNum, legal), depth, agentNum + 1))

		return score

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 9).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

