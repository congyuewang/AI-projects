#!/usr/bin/python

import copy
from heapq import *


class GBFS(object):
    
    def __init__(self, board):
        self.board = board
    
    def get_next_board(self):
        heap = []
        
        
        for i in range(0, self.board.length):
            for j in range(0, self.board.length):
                new_board = copy.deepcopy(self.board)
                if new_board.valid_square(i, j):
                    heappush(heap, new_board)
        
        
        target = heappop(heap)
        target.set_pl(self.board.pl1)
        
        return target

    @staticmethod
    def output_next_state(board):
        output_filename = './next_state.txt'
        wfile = open(output_filename, "w")
        for i in range(0, len(board.board)):
            if i == len(board.board) - 1:
                wfile.write("".join(board.board[i]))
            else:
                wfile.write("".join(board.board[i]) + "\n")

