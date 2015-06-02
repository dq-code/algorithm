from enum import Enum

class TicTacToe{
	class CellMark(Enum):
		X = 1
		EMPTY = 0
		O = -1
	
	def __init__(self):
    	self.__board = [[0 for x in range(3)] for x in range(3)]
        self.__play = CellMark.EMPTY
        self.clearBoard()
    
    def clearBoard(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                self.__board[i][j]=EMPTY
        self.__player = CellMark.X
    
}