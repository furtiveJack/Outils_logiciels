# Ariane and the Minotaur(s)

The purpose of this project is to implement a "puzzle" game with an automatic solution finding algorithm 
(automatic solver).

-----------------------------------------------------------------------------------------------------------------

## How to play

### Overview :

* There are 4 ways of running this program : 
    * [Play a classic game.](#classic-game)
        * [Commands](#commands)
    * [Find a solution using one of the solver.](#solvers)
        * [Using the naive solver.](#naive-solver)
        * [Using the minimal solver.](#minimal-solver)
    * [Run a benchmark to compare both solvers.](#benchmark)

* To start a new game, you should provide the map you want to use to play.

    * They are all located in the __maps__ folder.

* The rules of the game are specified in [project.pdf](project.pdf) (_in french_).

-----------------------------------------------------------------------------------------------------------------

### Classic game

To start the game and play Ariane yourself, you need to run the following command : 

```shell script
python3 ariane.py path_of_the_map classic
```                                            

#### Commands 

##### Move

To move (cell by cell) Ariane, you need to use the arrow keys.

##### Cancel a move

You can cancel your last move by pressing 'c' on your keyboard.

##### Create saves

You can save the current configuration of the game into a file,
and reload it later. To create a save, just press the 's' button while playing.

##### Load a save

When you launch the game with a given map, the game will search for a save matching 
the given map, and if it exists, you can choose to use it.

This means you can only create one save per map.

##### Clue feature

For each configuration of the game (_ie: after each one of your moves_), a solver
checks if you can still win regarding the current configuration. 

If not, the game is consider as lost. 

-----------------------------------------------------------------------------------------------------------------
### Solvers

To start one of the solver, use the following command :

```shell script
python3 ariane.py path_of_the_map solver_type [-v]
``` 

* __path_of_the_map__ : path to the map you want to use.
* __solver_type__ : choose the type of solver : [naive](#naive-solver) or [minimal](#minimal_solver).
* __-v__ : add this option if you want to visualize each computation step of the solver.

If you added the -v option, then you will visualize each computation step of the algorithm (this 
takes much more time though). Otherwise, you will quickly know if the map has a solution or not.

Once the computation is done, the algorithm returns a list of moves that lead to the victory, from the
initial configuration of the game.

You can use them during one of your own game on this map, or you can let the solver play the
game for you using this list of moves.


#### Naive Solver

The naive solver uses a backtracking search-algorithm (or Depth-First Search algorithm).

It uses recursion to compute all the possibles moves of Ariane from a given game configuration, and
continues until it finds a solution, or no solution at all.

To start the naive solver : 
```shell script
python3 ariane.py path_of_the_map naive [-v]
```

This solver returns a solution that works, but that may be longer (in terms of number of moves) than needed.

#### Minimal Solver

The minimal solver uses a breadth-first search-algorithm.

It compute all the sequences of possible moves ordered by length, until it
finds a winning configuration.

To start the minimal solver :
```shell script
python3 ariane.py path_of_the_map minimal [-v]
```

This solver returns a solution that is minimal in relation to number of moves.

-----------------------------------------------------------------------------------------------------------------

### Benchmark

The maps located in the __maps/defi__ directory are really hard to solve, for
a human being.

You can use them to make a benchmark of both algorithm :  compare their time and the results
they get.

You can add new maps in this folder if you want to.
To be usable by the benchmark, your maps must respect this naming convention : 
```shell script
defiXX.txt
```
where 'XX' is not an id for another map in this directory.

To run a benchmark :
```shell script
python3 ariane.py benchmark
```

You should get a result that looks like that : 

| File name         | DFS results               |           BFS results             |
|:-----------------:|:--------------------------|:----------------------------------|
| defi00.txt 	    | 208 moves	(58ms)	        |	    36 moves	(84ms)          |
| defi01.txt 	    | No solution	(100ms) 	|	 	No solution	(71ms)          |
| defi02.txt 	    | 177 moves	(26ms)	        |	 	93 moves	(150ms)         |
| defi03.txt 	    | 265 moves	(43ms)          |		41 moves	(170ms)         |
| defi04.txt 	    | 288 moves	(180ms)         |		102 moves	(271ms)         |
| defi05.txt 	    | 335 moves	(135ms)         |       85 moves	(180ms)         |
| defi06.txt 	    | 137 moves	(19ms)          |       33 moves	(64ms)          |
| defi07.txt 	    | 132 moves	(75ms)          |       100 moves	(116ms)         |
| defi08.txt        | 225 moves	(192ms)	        |       75 moves	(393ms)         |
| defi09.txt 	    | 272 moves	(142ms)	        |       106 moves	(114ms)         |
| defi10.txt 	    | 270 moves	(100ms)         |       88 moves	(209ms)         |
| defi11.txt 	    | 202 moves	(83ms)          |       74 moves	(79ms)          |
| defi12.txt 	    | 94 moves	(34ms)          |       48 moves	(189ms)         |

You can see that the number of moves provided by the minimal solver is really smaller
than for the naive solver, but it takes more time to compute.

So if you just want to know if the game has a solution, you should use the DFS algorithm.
If you want to know if it has a solution, AND play this solution, you should use the BFS algorithm.