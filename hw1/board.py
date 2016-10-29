#!/usr/bin/python
#import sys
import sys


class Board(object):
    int_min = -sys.maxint - 1
    int_max = sys.maxint
    
    def __init__(self, board, values, pl, last_positionX = 0, last_positionY = 0):
        self.board = board
        self.values = values
        self.length = len(board)
        self.last_positionX = last_positionX
        self.last_positionY = last_positionY
        
        if pl == 'X':
            self.pl1 = 'X'
            self.pl2 = 'O'
        if pl == 'O':
            self.pl1 = 'O'
            self.pl2 = 'X'
        
        self.max_pl = pl
        self.evaluation = self.get_evaluation()
    
    def set_pl(self, pl):
        if pl == 'X':
            self.pl1 = 'X'
            self.pl2 = 'O'
        else:
            self.pl1 = 'O'
            self.pl2 = 'X'

    def switch_pl(self):
        
        self.pl1,self.pl2=self.pl2,self.pl1
    
    
    
    def valid_square(self, x, y):
        if (x < 0) or (x >= self.length) or (y < 0) or (y >= self.length) or self.board[x][y]!='*':
            return False
        
        if self.board[x][y] == '*':
            if self.check_raid(x, y):
                self.apply_raid(x, y)
            else:
                self.apply_sneak(x, y)
            self.evaluation = self.get_evaluation()
            self.last_positionX = x
            self.last_positionY = y
            return True


    def check_raid(self, x, y):
        if x-1<0:
            up='*'
        else:
            up=self.board[x-1][y]


        if x+1>=self.length:
            down='*'
        else:
            down=self.board[x+1][y]

        if y-1<0:
            left='*'
        else:
            left=self.board[x][y-1]


        if y+1>=self.length:
            right='*'
        else:
            right=self.board[x][y+1]

 

        if (up == self.pl1) or (down == self.pl1) or (left == self.pl1) or (right == self.pl1):
            return True
        else:
            return False

    def apply_raid(self, x, y):
        self.board[x][y] = self.pl1
        if x-1<0:
            up='*'
        else:
            up=self.board[x-1][y]
            
            
        if x+1>=self.length:
                down='*'
        else:
            down=self.board[x+1][y]
            
        if y-1<0:
                left='*'
        else:
            left=self.board[x][y-1]
                
            
        if y+1>=self.length:
                right='*'
        else:
            right=self.board[x][y+1]
            
        
        if up == self.pl2:
            self.board[x - 1][y] = self.pl1
        if down == self.pl2:
            self.board[x + 1][y] = self.pl1
        if left == self.pl2:
                self.board[x][y - 1] = self.pl1
        if right == self.pl2:
            self.board[x][y + 1] = self.pl1

    def apply_sneak(self, x, y):
        self.board[x][y] = self.pl1
    
    def get_evaluation(self):
        evaluation = 0
        
        for i in range(0, self.length):
            for j in range(0, self.length):
                if self.board[i][j] == self.max_pl:
                    evaluation += self.values[i][j]
                elif self.board[i][j] != "*":
                    evaluation -= self.values[i][j]
    
        return evaluation

    def get_evaluation_string(self):
        if self.evaluation == self.int_max:
            return "Infinity"
        if self.evaluation == self.int_min:
            return "-Infinity"
        return self.evaluation

    def set_evaluation(self, evaluation):
        self.evaluation = evaluation
    
    def get_board_string(self):
        board_string = ""
        for i in range(0, self.length):
            board_string += "".join(self.board[i]) + "\n"
        
        return board_string
    
    def __str__(self):
        output = "The state of board is:\n"
        for i in range(self.length):
            output += ' '.join(self.board[i]) + "\n"
        return output
    
    def __cmp__(self, other):
        if self.evaluation < other.evaluation:
            return 1
        elif self.evaluation > other.evaluation:
            return -1
        else:
            if self.last_positionX < other.last_positionX:
                return -1
            elif self.last_positionX > other.last_positionX:
                return 1
            else:
                if self.last_positionY < other.last_positionY:
                    return -1
                elif self.last_positionY > other.last_positionY:
                    return 1

        return 0

