# 15-Puzzle Solver using Weighted A* Algorithm

This project implements the Weighted A* search algorithm with graph search to solve the 15-puzzle problem. The heuristic function used is the Sum of Chessboard distances of the tiles from their goal positions. The value of W is an input parameter in the implementation.

# Problem Description

On a 4x4 board, there are 15 tiles numbered from 1 to 15 and a blank position. A tile can slide into the blank position if it is horizontally or vertically adjacent to the blank position. Given a start board configuration and a goal board configuration, the objective is to find a move sequence with a minimum number of moves to reach the goal configuration from the start configuration.

# Usage

The program reads in the value for W, the initial and goal states from a text file that contains 11 lines. The output file contains 15 lines. The program uses Python language.

# Input file format

The input file should contain 11 lines:

    Line 1: value for W
    Line 2: blank
    Lines 3-6: tile pattern for the initial state
    Line 7: blank
    Lines 8-11: tile pattern for the goal state

# Output file format

The output file contains 15 lines:

    Lines 1-4: tile pattern for the initial state
    Line 5: blank
    Lines 6-9: tile pattern for the goal state
    Line 10: blank
    Line 11: W value from the input file
    Line 12: depth level d of the shallowest goal node as found by the search algorithm
    Line 13: total number of nodes N generated in the tree (including the root node)
    Line 14: solution (a sequence of actions from root node to goal node) represented by A’s. The A’s are separated by blank spaces. Each A is a character from the set {L, R, U, D}, representing the left, right, up and down movements of the blank position.
    Line 15: f(n) values of the nodes along the solution path from the root node to the goal node, separated by blank spaces. There should be d number of A values in line 14 and d+1 number of f values in line 15.
