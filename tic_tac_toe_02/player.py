import random
import math
class Player:
    def __init__(self,letter):
        self.letter = letter
        # here letter is x or o
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        sqaure = random.choice(game.available_moves())  
        return sqaure 

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        # the valid_square tells if the user's input is an actual valid or not,
        # for that we use try and catch block with a while loop, till its a valid square
        while(not valid_square):
            square = input(self.letter + '\'s turn. give an Input between [0 8]: ')
            try:
                val = int(square) #if its uncastable, say user enters some character rather than integer, it goes into catch block
                if val not in game.available_moves():
                    raise ValueError
                # if the controller has come here, that means everything is good
                valid_square = True
                
            except ValueError:
                print("Invalid input, try again!!")   
        return val 
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) 

    def get_move(self, game):
        if(game.count_empty_squares() == 9):
            square = random.choice(game.available_moves())
        else:
            # we have to get the square based on the minimax algorithm
            square = self.minmax(game, self.letter)['position'] # since its map

        return square  

    def minmax(self,state, player):
        max_player = self.letter #you yourself want to win!!
        other_player = 'X' if player == 'O' else 'O'

        #since this is a recursion method, we need a base case
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.count_empty_squares() + 1) if other_player == max_player else -1 * (state.count_empty_squares() + 1)
            }  
        elif(not state.is_empty_squares()):
            return{'position': None,
                   'score': 0}
        
        if(player == max_player):
            best = {'position': None, 'score': -math.inf} #each score should maximize
        else:
            best = {'position': None, 'score': math.inf} #each score should minimize

        for possible_move in state.available_moves():
            # now we here do kind of do back tracking
            #do something, see how it goes, undo it later try next move
            state.make_move(possible_move, player)
            sim_score = self.minmax(state, other_player)
            #now we undo
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #updating the dictionary if necessary
            if player == max_player: #maximizing the max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score   

        return best                  







        
  

