# HANGMAN GAME
from collections import namedtuple
import main

game_board = namedtuple('game_board', ['board', 'mistakes', 'letters', 'status'])
def welcome():
    """Starts the game."""
    print("Welcome")
    word = main._choose_word()
    _print_start_game()
    _print_start_spaces(word)
    game_board.letters = []
    game_board.mistakes = -1
    game_board.status = True
    while game_board.status:
        user_input = input("Guess a letter. To get a hint, type hint. To quit, type QUIT: \n").lower()
        if user_input != 'QUIT' and user_input != 'hint' and user_input != "\n":
            print('You guessed:', user_input, '\n')
            _check_input(user_input, word)
            _update_blank_spaces(user_input, word)
        elif user_input == 'hint':
            hint = main._hint(word)
            print(hint.upper())
            _print_board()
            _update_blank_spaces(user_input, word)
        else:
            print("Thanks for playing!")
            game_board.status = False
    print("Your word was: ", word)
    print('GAME OVER')


def _print_start_game() -> None:
    """Prints the starting game board."""
    top = ' _____\n'
    hang1 = '|     |\n'
    hang2 = '|     |\n'
    leg1 = '      |\n'
    leg2 = '      |\n'
    leg3 = '      |\n'
    stand = '______\n'

    game_board.board = [top + hang1 + hang2 + leg1 + leg2 + leg3 + stand]
    _print_board()

def _print_start_spaces(word) -> None:
    for spaces in word:
        if spaces == " ":
            print(" ", end='')
        else:
            print("_ ", end='')
    print()
    print()


def _check_input(user_input: str, word: str):
    """Checks if there is or isn't a wrong answer."""
    count_letters = 0
    for letters in word:
        if user_input == letters:
            count_letters += 1
    if count_letters > 1:
        print('You guessed correctly:', count_letters, 'letters\n')
    else:
        print('You guessed correctly:', count_letters, 'letter\n')

    if count_letters == 0:
        _wrong_answers()

    else:
        game_board.letters.append(user_input)
        _print_board()



def _wrong_answers():
    """Prints the man on the hangman board."""
    game_board.mistakes += 1
    top = '  ____\n'
    hang1 = ' |    |\n'
    hang2 = ' |    |\n'
    top_body = top + hang1 + hang2
    wrong_answers = [' o    |\n',' |    |\n', '\|    |\n', '\|/   |\n', '/     |\n', '/ \   |\n', ' _____\n']
    rest_of_body = ['      |\n', '      |\n', ' _____\n']
    if game_board.mistakes == 0:
        game_board.board = [top_body + wrong_answers[0] + rest_of_body[0] + rest_of_body[1] + rest_of_body[2]]
        _print_board()
    elif game_board.mistakes == 1:
        game_board.board = [top_body + wrong_answers[0] + wrong_answers[1]+ rest_of_body[1] + rest_of_body[2]]
        _print_board()
    elif game_board.mistakes == 2:
        game_board.board = [top_body + wrong_answers[0] + wrong_answers[2] + rest_of_body[1] + rest_of_body[2]]
        _print_board()
    elif game_board.mistakes == 3:
        game_board.board = [top_body + wrong_answers[0] + wrong_answers[3] + rest_of_body[1] + rest_of_body[2]]
        _print_board()
    elif game_board.mistakes == 4:
        game_board.board = [top_body + wrong_answers[0] + wrong_answers[3] + wrong_answers[4] + rest_of_body[2]]
        _print_board()
    elif game_board.mistakes == 5:
        game_board.board = [top_body + wrong_answers[0] + wrong_answers[3] + wrong_answers[5] + rest_of_body[2]]
        _print_board()
        _game_over()

def _update_blank_spaces(user_input, word):
    """Prints out the letter spaces."""
    for letter in word:
        if letter == user_input:
            print(letter, end='')
        elif letter in game_board.letters:
            print(letter, end='')
        elif letter == ' ':
            print(" ", end='')
        else:
            print('_ ', end='')

    print()
    print()
    _check_winner(word)

def _print_board():
    """Prints the board."""
    for piece in game_board.board:
        print(piece)

def _check_winner(word):
    """Checks if there is a winner."""
    how_many = 0
    for letter in word:
        if letter in game_board.letters:
            how_many += 1
        if letter == " ":
            how_many += 1
    if how_many == len(word):
        print('WINNER')
        game_board.status = False

def _game_over():
    """Ends game."""
    game_board.status = False


if __name__ == "__main__":
    welcome()

