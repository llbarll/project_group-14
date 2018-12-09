from itertools import groupby, chain

NONE = '.'
RED = 'R'
YELLOW = 'Y'

def diagonalsPos (matrix, cols, rows):
        """Get positive diagonals, going from bottom-left to top-right."""
        for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
                yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def diagonalsNeg (matrix, cols, rows):
        """Get negative diagonals, going from top-left to bottom-right."""
        for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
                yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]
def game(cols=7,rows=6,ToWin=4,board=[]):
        Cols=cols
        Rows=rows
        Win=ToWin
        board=[[NONE]*rows for _ in range(cols)]
        def insert(board,column,color):
                """insert color to given column"""
                c=board['board'][column]
                if c[0] != NONE:
                        raise Exception('Column is full!')
                i=-1
                while c[i] != NONE:
                        i-=1
                c[i] = color
                board['CheckForWin'](board)
        def checkForWin (board):
                """Check the current board for a winner."""
                w = board['getWINNER']()
                if w:
                        board['print_board']()
                        raise Exception(w + ' WINNER!!!!')
        def get_winner():
                """Get the winner on the current board."""
                lines = (board,zip(*board),
                         diagonalsPos(board,Cols,Rows),diagonalsNeg(board,Cols,Rows))
                for line in chain(*lines):
                        for color, group in groupby(line):
                                if color != NONE and len(list(group)) >= Win:
                                        return color
        def print_Board():
                """Print the board."""
                print('  '.join(map(str, range(Cols))))
                for y in range(Rows):
                        print('  '.join(str(board[x][y]) for x in range(Cols)))
                print()
        return {'board':board,'insert':insert,'CheckForWin':checkForWin,
                'getWINNER':get_winner,'print_board':print_Board}

if __name__ == '__main__':
        turn=RED
        g = game()
        while True:
                g['print_board']()
                row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
                if int(row) not in range(7):
                        print("Error,enter again")
                        continue
                try:
                        g['insert'](g,int(row), turn)
                except:
                        print("try again")
                        continue
                turn = YELLOW if turn == RED else RED
                
                
        
