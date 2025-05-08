
def compare_codes(code, guess):
    """
    Compare two Mastermind codes.

    Args:
        code (str): The secret code.
        guess (str): The guessed code.

    Returns:
        tuple: (correct, correct-ish)
            correct (int): Number of perfectly matching colors.
            correct-ish (int): Number of colors that appear in the code, but not in the correct position.
    """
    correct = 0
    correct_ish = 0
    code_list = list(code)
    guess_list = list(guess)

    # Count perfect matches
    for i in range(len(code)):
        if code_list[i] == guess_list[i]:
            correct += 1
            code_list[i] = None
            guess_list[i] = None

    # Count correct-ish matches
    for i in range(len(code)):
        if guess_list[i] is not None:
            if guess_list[i] in code_list:
                correct_ish += 1
                code_list[code_list.index(guess_list[i])] = None
                guess_list[i] = None

    return correct, correct_ish
