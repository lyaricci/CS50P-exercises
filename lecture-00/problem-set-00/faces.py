def main():
    """
    It prompts the user to enter some text that includes either ':)' or ':('.
    The function keeps looping until the user enters either ':)' or ':('.
    Once the user enters either of these emoticons,
    the function calls the 'convert()' function with the entered text
    as a parameter and prints the converted text to the console.
    """

    user_input = ''

    while ':)' not in user_input and ':(' not in user_input:
        user_input = input('Write something with :) or :( : ')

    print(convert(user_input))


def convert(string):
    """
    This function takes a string as input and replaces all occurrences of ':)'
    with the smiling face emoji '🙂' and all occurrences of ':('
    with the frowning face emoji '🙁'. The converted string is then
    returned by the function.

    Args:
        string (str): The input string that needs to be converted.

    Returns:
        str: The converted string with all occurrences of ':)' replaced by '🙂' and all occurrences of ':(' replaced by '🙁'.
    """

    string = string.replace(':)', '🙂')
    string = string.replace(':(', '🙁')
    return string
