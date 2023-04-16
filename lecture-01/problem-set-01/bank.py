def main():
    """
    This function prompts the user for a greeting
    and checks it using the 'check_string' function.
    """

    user_input = input("Greeting: ").lower().lstrip()
    check_string(user_input)


def check_string(string):
    """
    This function checks the given string and prints a corresponding
    monetary value based on its conditions.
    If the string starts with 'hello', it prints '$0',
    if it starts with 'h', it prints '$20', and otherwise it prints '$100'.

    Args:
        string (str): A string to be checked.
    """

    if string.startswith("hello"):
        print("$0")
    elif string.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
