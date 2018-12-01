# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    from util import Stack
    stack = Stack()
    visited = set()
    actions = []


    # Init stack and visited set
    stack.push(((problem.getStartState(), problem.getSuccessors(problem.getStartState()))))
    visited.add(problem.getStartState())

    # Start DFS
    while not stack.isEmpty():
        cur_state, neighbor = stack.list[-1]
        # Avoid repeat visitting same node
        valid_neighbor = filter(lambda x: x[0] not in visited, neighbor)
        for nxt in valid_neighbor:
            # Check goal, if next node is goal, do not need to visit it
            if problem.isGoalState(nxt[0]):
                actions.append(nxt[1])
                return actions
            stack.push((nxt[0], problem.getSuccessors(nxt[0])))
            actions.append(nxt[1])
            visited.add((nxt[0]))
            break
        # If no more valid node to be visited, should pop that node from stack
        if len(valid_neighbor) == 0:
            stack.pop()
            actions.pop()
    # If no valid path can be found, return empty path
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    queue = Queue()
    visited = set()

    startState = problem.getStartState()

    # Init queue and visited set
    queue.push((startState, []))
    visited.add(startState)

    # Start BFS
    while not queue.isEmpty():
        cur_state, path = queue.pop()
        if problem.isGoalState(cur_state):
            return path
        # Avoid repeat visitting same node
        valid_neighbor = filter(lambda x: x[0] not in visited, problem.getSuccessors(cur_state))
        for nxt in valid_neighbor:
            queue.push((nxt[0], path + [nxt[1]]))
            visited.add(nxt[0])
    # If no valid path can be found, return empty path
    return []


def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    pq = PriorityQueue()
    res = dict()
    visited = set()

    # Init queue and visited set
    pq.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
    res[problem.getStartState()] = []

    # Start A*
    while not pq.isEmpty():
        cur_state = pq.pop()
        path = res[cur_state]
        visited.add(cur_state)
        if problem.isGoalState(cur_state):
            return path

        valid_neighbor = filter(lambda x: x[0] not in visited, problem.getSuccessors(cur_state))
        for nxt in valid_neighbor:
            npath = path + [nxt[1]]
            np = problem.getCostOfActions(npath) + heuristic(nxt[0], problem)
            # Update both path and priority queue
            if nxt[0] not in res or (nxt[0] in res and problem.getCostOfActions(res[nxt[0]]) > np):
                res[nxt[0]] = npath
            pq.update(nxt[0], np)
    # If no valid path can be found, return empty path
    return []


def biDirectionalSearchMM0(problem, heuristic):
    """
    """
    heuristic = None
    pass

def biDirectionalSearchMM(problem, heuristic):
    pass

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bd0 = biDirectionalSearchMM0
bd = biDirectionalSearchMM
