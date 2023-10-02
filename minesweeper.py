import random
import re
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set() # to keep a track og places where e dug

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]  
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size*2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            # we use 8 to represnt the bomb
            if board[row][col] == '*':
                continue

            # now plant the bomb
            board[row][col] = '*'
            bombs_planted += 1
        return board 

    def assign_values_to_board(self):
        for i in range(self.dim_size):
            for j in range(self.dim_size):
                if(self.board[i][j] == '*'):
                    continue #since no point as its already a bomb
                self.board[i][j] = self.get_num_neighboring_bombs(i,j)

    def get_num_neighboring_bombs(self,i,j):
        count = 0
        for r in range(i-1, (i+1)+1):
            for c in range(j-1, (j+1)+1):
                if(r>=0 and r < self.dim_size and c>=0 and c < self.dim_size):
                    if(r == i and c == j):
                        continue
                    if(self.board[r][c] == '*'):
                        count+=1
        return count 

    def dig(self,row,col):
        self.dug.add((row,col))
        # if its a bomb then its game over and we return false
        if(self.board[row][col] == '*'):
            return False
        # if we dig at a place where the number > 0, means that there is a neighbouring bomb and its a successfull dig
        elif(self.board[row][col] > 0):
            return True
        
        # now we come here if the place is not a bomb and there are no neighbouring bombs as well
        # so we dig further till we find
        for r in range(row-1, (row+1)+1):
            for c in range(col-1, (col+1)+1):
                if(r>=0 and r < self.dim_size and c>=0 and c < self.dim_size):
                    if((r,c) in self.dug):
                        #means alread dug
                        continue
                    self.dig(r,c)
        return True            

    def __str__(self):
        # when ever you call print function on this object, it prints what ever this function returns
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                     visible_board[row][col] = ' '   

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep             




def play(dim_size = 10, num_bombs = 10):
    board = Board(dim_size, num_bombs)  
    safe = True
    # now we show the user the board and ask him for where to dug
    while( len(board.dug) < board.dim_size ** 2 - num_bombs):
        print(board)
        # handles 0,0 0, 0 or 0,   0
        user_input = re.split(',(\\s)*', input("where would you like to dig, Provide a input rpw,col in range [0-9]: "))
        #above line is a regex it looks for comma to split and \\s stands for white space
        # (\\s)* means 0 or all white spaces
        row, col = int(user_input[0]), int(user_input[-1]) # just to make sure if there is junk in between
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location, try again!")
            continue

        # now its a valid, so we dig
        safe = board.dig(row,col)
        if not safe:
            #its a bomb
            break

    if safe:
        print("you have Won")
    else:
        print(" you have dug a bomb, game Over! :(")
        # now lets reveal the whole board
        # but our print only sees in the dug set, lets add them in the set before we display
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__' :
    play() #explanation is that its good practice, when you have many files under your project and many imports, refer to the video at 1 hr 50 min















                     


