from random import seed, shuffle
seed(1001) # Ensures random selection is reproducible 

HIDDEN = 'X'
HELP_COMMAND = 'h'
QUIT_COMMAND = 'q'

WELCOME_MESSAGE = "Welcome to Memory Mash."
SIZE_PROMPT = "Please enter a game size between 1 to 9: "
COMMAND_PROMPT = "Please enter command: "
WIN_MESSAGE = "You have revealed all cards!"
INVALID_MESSAGE = "Invalid Command! Enter h for command format."
HELP_MESSAGE = """
- h/H: Display Help Message
- q/Q: Quit Current Game
- [R1],[C1] [R2],[C2] ... [RN],[CN]: Flip cards at given coordinates. 
        [RX] is row of card X, [CX] is column of card X. N is number of sets.
"""
AGAIN_PROMPT = "Would you like to play again? (y/n): "


def generate_hidden_state(game_size: int) -> list[list[str]]:
    """
    Generates the hidden state for a new game of Memory Mash.

    Args:
        game_size (int): Number of matching sets for new game. 
                Precondition: game_size > 0

    Returns:
        list[list[str]]: Layout of facedown cards
    """
        
    # Generate all cards
    cards = []
    for i in range(game_size):
        cards += [str(i+1)] * game_size

    shuffle(cards)

    # Reshape cards into square
    state = []
    for i in range(game_size):
        state.append(cards[game_size*i:game_size*(i+1)])

    return state