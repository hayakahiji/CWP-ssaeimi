#!/usr/bin/env python3

class Piece:
    #Constructor
    def __init__(self, x, y):        
        self.x = x
        self.y = y
    #Method
    def can_attack(self, king, board):
        return False
    
class King(Piece):
    def __init__(self, x, y): # Inheritance from Piece class
        super().__init__(x, y)
        
class Rook(Piece):
    def __init__(self, x, y): # Inheritance from Piece class
        super().__init__(x, y)
    
    def can_attack(self, king, board):
        # check row
        if self.x == king.x:
            step = 1 if king.y > self.y else -1
            
            for col in range(self.y + step , king.y):
                # มีตัวขวาง
                if board[self.x][col] in mapping:
                    return False
            return True
        # check col
        if self.y == king.y:
            step = 1 if king.x > self.x else -1
            
            for row in range(self.x + step , king.x + step):
                # มีตัวขวาง
                if board[self.x][row] in mapping:
                    return False
            return True
        return False
                 
         
class Bishop(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def can_attack(self, king, board):
        dx = king.x - self.x
        dy = king.y - self.y
        if abs(dx) != abs(dy):    # check ว่าทแยงไหม ถ้าทแยง ผลต่างระหว่าง row,col ต้องเท่ากัน              
            return False
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        
        row, col = self.x + step_x, self.y + step_y
        while row != king.x and col != king.y:
            # มีตัวขวาง
            if board[row][col] in mapping:              
                return False
            row += step_x
            col += step_y
        return True

class Queen(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def can_attack(self, king, board):
        # Queen = Rook ∪ Bishop
        return (Rook(self.x, self.y).can_attack(king, board) or
                Bishop(self.x, self.y).can_attack(king, board))

        
class Pawn(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def can_attack(self, king, board):
        # กินทแยง only
        return (king.x,king.y) in [
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y + 1),
        ]
        
        
mapping = {"K": King, "R": Rook, "B": Bishop, "Q": Queen, "P": Pawn}

def checkmate(board_str: str):
    board = [list(row.strip()) for row in board_str.strip().split("\n")]
    size = len(board)

    pieces = []
    king = None

    for i in range(size):
        # check ว่าเป็นกระดานไหม
        if(size != len(board[i])):
            print("Error")
            return
        # ใส่หมากแต่ละตัวลงกระดาน
        for j in range(size):
            c = board[i][j]
            if c in mapping:
                piece = mapping[c](i, j)   # i=row=x, j=col=y
                if c == "K":
                    king = piece
                else:
                    pieces.append(piece)

    if not king:
        print("Error")
        return

    for p in pieces:
        if p.can_attack(king, board):
            print("Success")
            return

    print("Fail")
        
        
        

                    
                
            
            