from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # to keep track of the winner

    def print_board(self):
        # this prints the current state of the board
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            #in the above line we have just sliced our board into three parts
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    #we have used static method, bcoz its independent method as we only print the indices of positions
    # Also we need not need self in static
    def print_board_indexes():
        index_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in index_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']

    def is_empty_squares(self):
        return ' ' in self.board

    def count_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if(self.board[square] == ' '):
            self.board[square] = letter
            if(self.winner(square,letter)):
                self.current_winner = letter
            return True
        return False  

    def winner(self,square,letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if( all([spot == letter for spot in row])):
            return True
        # now we check for col wise

        col_ind = square % 3 
        col = [self.board[col_ind+(i*3)] for i in range(3)]
        if( all([spot == letter for spot in col])):
            return True
        #now we check for diagonally

        if(square % 2 == 0):
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if( all([spot == letter for spot in diagonal1])):
                return True
            if( all([spot == letter for spot in diagonal2])):
                return True

        return False    

def play(game, x_player, o_player, print_game = True):
    if(print_game):
        game.print_board_indexes()
    # print game is introduced to make sure that, if we really want to print our board or not
    letter = 'X' #assume its the starting point

    while(game.is_empty_squares):
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if(game.make_move(square, letter)):
            if(print_game):
                print(letter + f" makes a move to square {square}")
                game.print_board()  
                print('') # for new line 
            if(game.current_winner):
                if(print_game):
                    print(letter + ' is the winner!')   
                return letter      
        # now that we have made a move we should give the chance to ther next people
        letter = 'X' if letter == 'O' else 'O'         
    
    if(game.current_winner == None and print_game):
        print('Its a tie!')

if(__name__ == '__main__'):
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    #o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    
    
