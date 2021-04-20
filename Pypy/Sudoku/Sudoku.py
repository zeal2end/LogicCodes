#!/usr/bin/python3

from copy import copy
from time import sleep

DIMENSION = 9
NCELL = DIMENSION**2
MAXC = DIMENSION+1

test = [
[0, 0, 6, 1, 0, 0, 3, 4, 5],
[8, 0, 1, 0, 4, 0, 7, 2, 0],
[0, 0, 3, 6, 0, 2, 8, 9, 1],
[5, 6, 0, 0, 2, 0, 9, 1, 3],
[3, 4, 2, 0, 0, 9, 0, 8, 7],
[0, 0, 7, 3, 0, 0, 0, 0, 0],
[0, 8, 0, 0, 0, 1, 4, 7, 0],
[0, 1, 0, 4, 6, 7, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#class board
class BoardType():
    """docstring for Board."""
    FINISHED = False
    def __init__(self,*args):
        if len(args) > 0:
            self.m = args[0]
            self.FreeCount = sum(list(a.count(0) for a in self.m))
        elif len(args) == 0:
            n = int(input("Enter the number of places you want to enter :"))
            matrix = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
            print("Format for input : x y z (where x y denotes coordinates and z in the value :).")
            for _ in range(n):
                a,b,x = map(int,input().split())
                matrix[a][b] = x
            self.m = matrix
            self.FreeCount = NCELL - n
        self.move = [[0,0] for _ in range(NCELL+1)] #inside init
        self.Index = -1
        self.move[self.Index] = self.next_square()

    def next_square(self): # this is to be update for more complex processing
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if not self.m[i][j]:
                    return [i,j]

    def printBoard(self):
        for a in self.m:
            print(a)

    def isASolution(self):
        return self.FreeCount == 0

    def findThree(self,a):
        for i in [0,3,6]:
            if a>=i and a <i+3:
                return i

    def Construct_Candidate(self):
        possible = [i for i in range(1,DIMENSION+1)]
        self.move[self.Index] = self.next_square() # bug noticed 0 is not set so it will go for it again.
        # checking row
        x,y = map(int,self.move[self.Index])
        abonded = list(filter(lambda c:c!=0,self.m[x]))
        #checking col
        abonded += [self.m[i][y] for i in range(DIMENSION) if self.m[i][y]!=0]
        #checking the inner cube
        x = self.findThree(x)
        y = self.findThree(y)
        for i in range(3):
            a = self.m[x+i][y:y+3]
            abonded += list(filter(lambda c:c!=0,a))
        return list(filter(lambda c:c not in abonded,possible))
        #done Construct_Candidate

    def make_move(self,x,y,a,b):
        self.m[x][y] = a
        self.FreeCount += b
        self.Index -=b


def Sudoku(Board):
    if Board.isASolution():
        Board.FINISHED = True
        Board.printBoard()
    else:
        cur = copy(Board.Index)
        possible = Board.Construct_Candidate()
        for a in possible:
            x,y = map(int,Board.move[cur])
            Board.make_move(x,y,a,-1)
            Sudoku(Board)
            Board.make_move(x,y,0,1)
            if Board.FINISHED: return


def main():
    Board = BoardType(test) #for testing insert the matrix test
    Sudoku(Board)

if __name__ == "__main__":
    main()
