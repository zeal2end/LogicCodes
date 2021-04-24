#!/usr/bin/python3
#AUTHOR OF THIS CODE zeal2end feel free to fork and make changes.
#TO RUN THIS CODE ON CUSTOM MATRIX REMOVE THE ARGS FROM BOARDTYPE IN MAIN() i.e Board = BoardType(test) -->> Board = BoardType()
# the test matrix is one of the hard sudoku puzzles and it will take some time around 10 sec to fully generate the ans.
# instructions for CUSTOM INPUT :
# this puzzle can still be pruned as we can still add conditions to the search wont go further on doomed solutions.
'''
    3
   0 4 7
   3 2 6
   2 6 8  where x y z is the format and x,y is the corrdinate in matrix
'''
from copy import copy
from time import sleep

DIMENSION = 9
NCELL = DIMENSION**2
MAXC = DIMENSION+1

test = [
[0, 0, 0, 0, 0, 0, 0, 1, 2],
[0, 0, 0, 0, 3, 5, 0, 0, 0],
[0, 0, 0, 6, 0, 0, 0, 7, 0],
[7, 0, 0, 0, 0, 0, 3, 0, 0],
[0, 0, 0, 4, 0, 0, 8, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 8, 0, 2, 0, 0, 0, 4, 0],
[0, 5, 0, 0, 0, 0, 6, 0, 0]
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
        self.Index = 0
        print("Sudoku Puzzle : ")
        self.printBoard()
        print("One of the Solution is : ")

    def next_square(self): # this is to be update for more complex processing nxt task
        best = [0,0]
        cur = 10
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.m[i][j] == 0:
                    now =len(self.Possible([i,j]))
                    if now < cur:cur = now;best = [i,j]
                    if now == 1:
                        return [i,j]
        return best

    def printBoard(self):
        for a in self.m:
            print(a)

    def isASolution(self):
        return self.FreeCount == 0

    def findThree(self,a):
        for i in [0,3,6]:
            if a>=i and a <i+3:
                return i

    #new candidate
    #first create a function to find possibles for a given x,y
    def Possible(self,pair):
        x,y=map(int,pair)
        considered = [i for i in range(1,10)]
        abonded = list(filter(lambda x : x!=0,self.m[x]))
        abonded += [self.m[i][y] for i in range(DIMENSION) if self.m[i][y]]
        x,y = self.findThree(x),self.findThree(y)
        for i in range(3):
            a = self.m[x+i][y:y+3]
            abonded += list(filter(lambda x:x!=0,a))
        return list(filter(lambda x:x not in abonded,considered))

    def Construct_Candidate(self):
        self.move[self.Index] = self.next_square()
        return self.Possible(self.move[self.Index])

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
        #print(possible,Board.move[Board.Index])
        # create a Construct_Candidate '''
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
