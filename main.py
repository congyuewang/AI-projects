#!/usr/bin/python

import sys
import getopt
import copy
from heapq import *
from board import Board
from GBFS import GBFS
from minimax import MiniMax
from alpha_beta import AlphaBeta


class main(object):
    board_length = 5
    GBFS = 1
    MINIMAX = 2
    ALPHA_BETA_PRUNING = 3
    BATTLE = 4

    def __init__(self):
        self.input_file = main.get_input_file()
        parameters = main.get_input_parameters(self.input_file)
        self.board = parameters["board"]

        # greedy best first search = 1
        # MiniMax = 2
        # Alpha-beta Pruning = 3
        # Battle = 4
        self.task_num = int(parameters["task_num"])

        if self.task_num == main.GBFS:
            self.depth = parameters["depth"]
            self.GBFS()
        elif self.task_num == main.MINIMAX:
            self.depth = parameters["depth"]
            self.minimax()
        elif self.task_num == main.ALPHA_BETA_PRUNING:
            self.depth = parameters["depth"]
            self.alpha_beta()
        elif self.task_num == self.BATTLE:
            self.depth1 = parameters["depth1"]
            self.depth2 = parameters["depth2"]
            self.task1 = parameters["task1"]
            self.task2 = parameters["task2"]
            self.pl1 = parameters["pl1"]
            self.pl2 = parameters["pl2"]
            self.battle()

    @staticmethod
    def get_input_file():
 
        return "./input.txt"           

    @staticmethod
    def get_input_parameters(input_file):
        parameters = {}
        readfile = open(input_file)
        # read task num
        parameters["task_num"] = int(readfile.readline().strip())
        if parameters["task_num"] < 4:
            pl1 = readfile.readline().strip()

            parameters["depth"] = readfile.readline().strip()

            board = list()
            values = list()
            # read board values
            for i in range(main.board_length):
                values.append([])
                for value in readfile.readline().split():
                    values[i].append(int(value))

            # read current state
            for i in range(main.board_length):
            #for i=0 : main.board_length:
                board.append(list(readfile.readline().strip()))

            parameters["board"] = Board(board, values, pl1)
        else:
            pl1 = readfile.readline().strip()
            task1 = int(readfile.readline().strip())
            depth1 = int(readfile.readline().strip())
            pl2 = readfile.readline().strip()
            task2 = int(readfile.readline().strip())
            depth2 = int(readfile.readline().strip())

            board = list()
            values = list()
            # read board values
            for i in range(main.board_length):
                values.append([])
                for value in readfile.readline().split():
                    values[i].append(int(value))

            # read current state
            for i in range(main.board_length):
                board.append(list(readfile.readline().strip()))

            parameters["board"] = Board(board, values, pl1)
            parameters["depth1"] = depth1
            parameters["depth2"] = depth2
            parameters["task1"] = task1
            parameters["task2"] = task2
            parameters["pl1"] = pl1
            parameters["pl2"] = pl2

        return parameters

    

            

    def GBFS(self):
        agent = GBFS(self.board)
        board = agent.get_next_board()
        agent.output_next_state(board)

    def minimax(self):
        agent = MiniMax(self.board, self.depth)
        board = agent.get_next_board()
        agent.output_next_state(board)
        agent.output_log()

    def alpha_beta(self):
        agent = AlphaBeta(self.board, self.depth)
        board = agent.get_next_board()
        agent.output_next_state(board)
        agent.output_log()

    def get_agent(self, task_id, board, depth):
        if task_id == self.GBFS:
            return GBFS(board)
        elif task_id == self.MINIMAX:
            return MiniMax(board, depth)
        else:
            return AlphaBeta(board, depth)

    def battle(self):
        board = copy.deepcopy(self.board)
        wfile = open("./trace_state.txt", "w")
        while self.not_finished(board.board):
            if board.pl1 == self.pl1:
                board.max_pl = self.pl1
                agent = self.get_agent(self.task1, board, self.depth1)
            else:
                board.max_pl = self.pl2
                agent = self.get_agent(self.task2, board, self.depth2)
            board = agent.get_next_board()
            board.switch_pl()
            wfile.write(board.get_board_string())

    def not_finished(self, board):
        for i in range(0, self.board_length):
            for j in range(0, self.board_length):
                if board[i][j] == "*":
                    return True
        return False


if __name__ == '__main__':
    main = main()
