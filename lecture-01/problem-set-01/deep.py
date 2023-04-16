def main():
    """
    Asks the user for an answer to the Great Question of Life, the Universe, and Everything,
    converts the answer to a lowercase string with no leading or trailing whitespace,
    and checks whether the answer is correct (42, "forty two", or "forty-two").
    Prints "YES" if the answer is correct, and "NO" otherwise.
    """

    user_input = input(
        'What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    user_input = convert_string(user_input)
    check_answer(user_input)


def convert_string(str):
    """
    Converts the input string to lowercase and removes leading and trailing whitespace.

    Args:
        str (str): A string to be converted.

    Returns:
        str: The converted string.
    """

    str = str.lower().strip()
    return str


def check_answer(answer):
    """
    Checks whether the given answer is correct (42, "forty two", or "forty-two").
    Prints "YES" if the answer is correct, and "NO" otherwise.

    Args:
        answer (str): The user's answer to the Great Question of Life, the Universe, and Everything.

    Returns:
        None
    """

    match answer:
        case '42' | 'forty two' | 'forty-two':
            print('YES')
        case _:
            print('NO')


main()
