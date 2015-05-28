"""
Implementation of Solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store
"""

import poc_mancala_gui

__author__ = "Matt Rathbun"
__email__ = "mrathbun80@gmail.com"
__version__ = "1.0"

class SolitaireMancala:
    """Simple class that implements Solitaire version of Mancala - Tchoukaillon"""

    def __init__(self):
        """Create game with empty store and no houses"""
        self._board = [0]

    def __str__(self):
        """Return a string representation of the board"""
        display_configuration = list(self._board)
        display_configuration.reverse()
        return str(display_configuration)

    def set_board(self, configuration):
        """
        Set the board using the supplied configuration
        The store corresponds to 0th index in the list
        The houses are indexed in ascending order from right to left
        """
        new_configuration = list(configuration)
        self._board = new_configuration

    def get_num_seeds(self, house_num):
        """Return the number of seeds in a specific house"""
        return self._board[house_num]

    def is_legal_move(self, house_num):
        """Determine if a move is legal from a specific house"""
        if house_num is 0:
            return False

        return self._board[house_num] == house_num

    def apply_move(self, house_num):
        """Apply a move from a specific house"""
        if house_num > 0:
            for house in range((house_num - 1), -1, -1):
                self._board[house] += 1

            self._board[house_num] = 0

    def choose_move(self):
        """Choose the best move available"""
        for house in range(1, len(self._board)):
            if self._board[house] == house:
                return house

        return 0

    def is_game_won(self):
        """Determine if the game is won"""
        for house in range(1, len(self._board)):
            if self._board[house] != 0:
                return False

        return True

    def plan_moves(self):
        """Return a list of legal moves that will win the game"""
        current_configuration = self._board
        temporary_configuration = list(current_configuration)
        moves = []

        self.set_board(temporary_configuration)

        while not self.is_game_won():
            next_move = self.choose_move()

            if next_move == 0:
                break

            self.apply_move(next_move)
            moves.append(next_move)

        self.set_board(current_configuration)

        return moves

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [0, 0, 1, 1, 3, 5, 0]
    config2 = [0, 2, 3, 4, 5, 6, 7]
    config3 = [6, 0, 0, 0, 0, 0, 0]
    config4 = [10, 2, 3, 4]
    my_game.set_board(config1)

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])

    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(4), "Expected:", False

    my_game.apply_move(5)

    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])

    my_game.apply_move(4)

    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 3, 3, 2, 2])

    my_game.set_board(config1)

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 5

    my_game.apply_move(5)

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1

    my_game.set_board(config2)

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 0

    my_game.set_board(config4)

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 0

    my_game.set_board(config1)

    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False

    my_game.set_board(config3)

    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", True

    my_game.set_board(config1)

    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", str([5, 1, 2, 1, 4, 1, 3, 1, 2, 1])

    my_game.set_board(config2)

    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", str([])

# test_mancala()
poc_mancala_gui.run_gui(SolitaireMancala())
