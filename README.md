# BiDirectionalSearch
A course project for ASU CSE571.
## Introduction
- BFS, DFS, A*, Bi-directional Search(MM and MM0) for pacman and Rubik's Cube.
- We reused pacman code from CSE571 course project1.
- Implemented 2-d Rubik's cube game interface.
## Prerequirement
- Python2 (Only python2)
## Important Locations
- Search algorithms for pacman located in `/pacman/search.py`.
- Problem class and heuristic function for pacman located in `/pacman/searchAgents.py`.
- Search algorithms and heuristic function for Rubik's cube located in `/cube/solver.py`.
- Layouts of pacman located in `\pacman\layouts`.
- Layouts of Rubik's cube located in `\cube\test`.
- Main entrances: `\pacman\pacman.py` and `\cube\rubikCube.py`.
- Auto tester for Rubik's cube, `\cube\test.py`(Python 3 required for running that tester).
## How to run project
### Pacman
We modified code from course project1, therefore, only one kind of problem (PositionSearchProblem) and one kind of heuristic function (foodHeuristic) can be supported. We only support 4 types of maze: tiny, small, medium and big.
Example:
- To run `bfs` test with medium size maze: `python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs,prob=PositionSearchProblem`.
- To run `dfs` test with tiny size maze: `python2 pacman.py -l tinyMaze -p SearchAgent -a fn=dfs,prob=PositionSearchProblem`.
- To run `astar` test with medium size maze: `python2 pacman.py -l mediumMaze -p SearchAgent -a fn=astar,prob=PositionSearchProblem,heuristic=foodHeuristic`.
- To run `bi-directional MM0` test with medium size maze: `python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs,prob=PositionSearchProblem`.
- To run `bi-directional MM` test with big size maze: `python2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs,prob=PositionSearchProblem,heuristic=foodHeuristic`.
## Team Members
- Yuan Cao [(@caoyuan0816)](https://github.com/caoyuan0816)
- Zelin Bao [(@baozelin)](https://github.com/baozelin)
- Yiru Hu [(@yiruhu)](https://github.com/yiruhu)
- Yiting Lin [@Yiting027](yiting.lin027@gmail.com)
