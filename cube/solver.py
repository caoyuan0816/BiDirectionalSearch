"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
rubikCube.py
--------------------------------------------------------------------------------
Solver functions for rubik's cube problem.
Including:
    BFS solver.
    DFS solver.
    A* solver.
    Bi-directional Search solver. (MM0 and MM)
"""
import copy

from cube import Cube

class Solver:
    """
    Abstract class solver.
    Define helper properties and functions for other solvers.
    """
    def __init__(self, cube):
        """
        Init values.
        """
        self.cube = cube
        self.result = None
        self.expanded = 0
        self.ops = ['F', 'B', 'R', 'L', 'U', 'D', 'rF', 'rB', 'rR', 'rL', 'rU', 'rD']
        self.rops = ['rF', 'rB', 'rR', 'rL', 'rU', 'rD', 'F', 'B', 'R', 'L', 'U', 'D']

    def solve(self):
        """
        Abstract method solve().
        All solvers have to implement this method to solve the probelm.
        """
        pass

    def getResult(self):
        """
        Return solver's result as a list of instructions.
        """
        return self.__parseInstructions(self.result)

    def __parseInstructions(self, instructions):
        """
        Used to parse instruction str to list.
        """
        res, i = [], 0
        while i < len(instructions):
            if instructions[i] == 'r':
                res.append(instructions[i]+instructions[i+1])
                i += 2
            else:
                res.append(instructions[i])
                i += 1
        return res

    def getNodeExpanded(self):
        """
        Return the number of node expanded after solver run.
        """
        return self.expanded


class breadthFirstSearch(Solver):
    """
    BFS solver for Rubik's Cube problem.
    """
    def solve(self):
        """
        implementation of BFS.
        """
        from collections import deque

        # Check start state whether or not is goal state
        if self.cube.isSolved():
            self.result = ''
            return True

        # Define visited set and que
        visited = set([self.cube.getLayout()])
        que = deque([(self.cube.getLayout(), '')])

        while len(que) != 0:
            # Pop current state from que
            cur_layout, cur_ops = que.popleft()
            cur_cube = Cube(cur_layout)

            # Expand neighbors of current state
            for o in range(12):
                # Apply operation to cube object
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                # Check valid
                if layout not in visited:
                    # Check solution
                    if Cube(layout).isSolved():
                        self.result = cur_ops+self.ops[o]
                        self.expanded = len(visited)
                        return True
                    # Update visited set and que
                    visited.add(layout)
                    que.append((layout, cur_ops+self.ops[o]))
                # Recover cube's state using reversed operation
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class depthFirstSearch(Solver):
    """
    DFS solver for Rubik's Cube problem.

    We implemented a recursively version of DFS.

    We also set a maximum searching level to reduce the time and memory cost.
    The value of maximum searching level equals to x for rand_x test data.
    """
    def __helper(self, layout, ops, visited, level, maxLevel):
        """
        Private helper to do the real recursively DFS search.
        """
        # Count node expanded for each new visiting node
        self.expanded += 1
        cube = Cube(layout)
        # Check terminal states
        if cube.isSolved():
            self.result = ''.join(ops)
            return True
        # Maximum level check
        if level == maxLevel:
            return False

        # Expand neighbors node
        for o in range(12):
            # Apply operation to cube object
            getattr(cube, self.ops[o])()
            cur_layout = cube.getLayout()
            if cur_layout not in visited:
                visited.add(cur_layout)
                # Recursion call for DFS
                if self.__helper(cur_layout, ops+[self.ops[o]], visited, level+1, maxLevel):
                     return True
                visited.remove(cur_layout)
            # Recover cube's state using reversed operation
            getattr(cube, self.rops[o])()

        return False

    def solve(self, maxLevel):
        """
        implementation of DFS.
        Run DFS using self.__helper().
        """
        return self.__helper(self.cube.getLayout(), [], set(), 0, maxLevel)


class aStarSearch(Solver):
    """
    Astar solver for Rubik's Cube problem.
    """
    def __heuristic(self, cube):
        """
        Heuristic function.
        It's hard to find a good heuristic function for solving Rubik's Cube.
        Therefore, we simply count the number of colors that different with goal.
        """
        count = 0
        for i in range(6):
            color = cube.cube[i][1][1]
            for j in range(3):
                for k in range(3):
                    if cube.cube[i][j][k] != color:
                        count += 1
        return count

    def __cost(self, depth):
        """
        Cost function.
        We use depth*5 instead of depth to avoid search in a wrong way for too deep.
        """
        return depth*5

    def solve(self):
        """
        implementation of Astart search.
        """
        import heapq

        # Check start state
        if self.__heuristic(self.cube) == 0:
            self.result = ''
            return True

        # Init visited set and priority que
        pq = [(self.__heuristic(self.cube), self.cube.getLayout(), '', 0)]
        visited = set([self.cube.getLayout()])

        while len(pq) != 0:
            # Get current state
            h, cur_layout, cur_ops, g = heapq.heappop(pq)
            cur_cube = Cube(cur_layout)

            # Expand neighbor nodes
            for o in range(12):
                # Pruning
                if len(cur_ops) != 0 and self.rops[o] == cur_ops[-1]:
                    continue
                # Apply op
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    # Check goal
                    if self.__heuristic(Cube(layout)) == 0:
                        self.result = cur_ops+self.ops[o]
                        self.expanded = len(visited)
                        return True
                    # Update priority que and visited set
                    visited.add(layout)
                    heapq.heappush(pq, (self.__heuristic(cur_cube)+self.__cost(g+1), layout, cur_ops+self.ops[o], g+1))
                # Recover by reversed op
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class biDirectionalSearchMM0(Solver):
    """
    Bi-directional Search solver

    MM0 Version.
    In MM0 version, we just do a simple BFS in two sides.
    """
    def solve(self):
        """
        implementation of bd-MM0
        """
        from collections import deque

        # Init queue, visited set and expanding level counter
        que1, que2 = deque([(self.cube.getLayout(), '', 0)]), deque([(Cube().getLayout(), '', 0)])
        visited1, visited2 = {self.cube.getLayout(): ''}, {Cube().getLayout(): ''}
        expanding_level1, expanding_level2 = 0, 0

        # We will run two BFS level expanding in each while round
        while True:
            # First BFS, from start to goal
            # Only expand one level
            if len(que1) == 0:
                self.result = None
                return False

            while len(que1) != 0 and que1[0][2] == expanding_level1:
                cur_layout, cur_ops, level = que1.popleft()
                cur_cube = Cube(cur_layout)

                # The meeting in the middle has been proved
                if cur_layout in visited2:
                    self.result = cur_ops + visited2[cur_layout]
                    self.expanded = len(visited1) + len(visited2)
                    return True

                for o in range(12):
                    getattr(cur_cube, self.ops[o])()
                    layout = cur_cube.getLayout()
                    if layout not in visited1:
                        visited1[layout] = cur_ops+self.ops[o]
                        que1.append((layout, cur_ops+self.ops[o], level+1))
                    getattr(cur_cube, self.rops[o])()
            expanding_level1 += 1

            # Second BFS, from goal to start
            # Only expand one level
            if len(que2) == 0:
                self.result = None
                return False

            while len(que2) != 0 and que2[0][2] == expanding_level2:
                cur_layout, cur_ops, level = que2.popleft()
                cur_cube = Cube(cur_layout)

                # The meeting in the middle has been proved
                if cur_layout in visited1:
                    self.result = visited1[cur_layout] + cur_ops
                    self.expanded = len(visited1) + len(visited2)
                    return True

                for o in range(12):
                    getattr(cur_cube, self.ops[o])()
                    layout = cur_cube.getLayout()
                    if layout not in visited2:
                        visited2[layout] = self.rops[o]+cur_ops
                        que2.append((layout, self.rops[o]+cur_ops, level+1))
                    getattr(cur_cube, self.rops[o])()
            expanding_level2 += 1

        self.result = None
        return False


class biDirectionalSearchMM(Solver):
    """
    Bi-directional Search solver

    MM Version.
    In MM version, we do two Astar search in both side.
    """
    def __heuristic(self, cube1, cube2=None):
        """
        Heuristic function.
        In MM, we define heuristic function as:
            the 'distance' between two states
            and 'distance' = number of misplaced color
        We know it's not a good heuristic function, but we tried.
        """
        if cube2 is None:
            cube2 = Cube()
        count = 0
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if cube1.cube[i][j][k] != cube2.cube[i][j][k]:
                        count += 1
        return count

    def __cost(self, depth):
        """
        Cost function.
        We use depth*5 instead of depth to avoid search in a wrong way for too deep.
        """
        return depth*5

    def solve(self):
        """
        implementation for bd-MM.
        """
        import heapq

        # Init two priority queues, visited sets
        pq1 = [(self.__heuristic(self.cube), self.cube.getLayout(), '', 0)]
        pq2 = [(self.__heuristic(Cube(), self.cube), Cube().getLayout(), '', 0)]

        visited1, visited2 = {self.cube.getLayout(): ''}, {Cube().getLayout(): ''}

        # Similar as bd-MM0, two Astar search each while round
        # But this time in each Astar search, we only expand one node
        #   instead of one level of nodes
        while True:
            # First round Astar search, from start to goal
            if len(pq1) == 0:
                self.result = None
                return False

            _, cur_layout, cur_ops, level = heapq.heappop(pq1)
            cur_cube = Cube(cur_layout)

            if cur_layout in visited2:
                self.result = cur_ops + visited2[cur_layout]
                self.expanded = len(visited1) + len(visited2)
                return True

            # Expand new nodes
            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited1:
                    visited1[layout] = cur_ops+self.ops[o]
                    # Calculate new priority value
                    np = self.__cost(level+1)+self.__heuristic(cur_cube)
                    heapq.heappush(pq1, (np, layout, cur_ops+self.ops[o], level+1))
                getattr(cur_cube, self.rops[o])()

            # Second round Astar search, from goal to start
            if len(pq2) == 0:
                self.result = None
                return False

            _, cur_layout, cur_ops, level = heapq.heappop(pq2)
            cur_cube = Cube(cur_layout)

            if cur_layout in visited1:
                self.result = visited1[cur_layout] + cur_ops
                self.expanded = len(visited1) + len(visited2)
                return True

            # Expand new nodes
            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited2:
                    visited2[layout] = self.rops[o]+cur_ops
                    # Calculate new priority value
                    np = self.__cost(level+1)+self.__heuristic(cur_cube, self.cube)
                    heapq.heappush(pq2, (np, layout, self.rops[o]+cur_ops, level+1))
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bd0 = biDirectionalSearchMM0
bd = biDirectionalSearchMM
