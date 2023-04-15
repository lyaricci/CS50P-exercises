def main():
    """
    It prompts the user to enter an integer value for mass (in kg) using the 'check_for_input()' function.
    It then calculates the equivalent energy (in Joules) using the mass
    and the speed of light constant.
    Finally, the function prints the equivalent energy to the console in a formatted string.
    """

    mass = check_for_input()

    light_speed = 300000000
    energy = mass * light_speed ** 2

    print(f'The equivalent energy is {energy} Joules.')


def is_valid_int(string):
    """
    This function takes a string as input and checks if it can be
    converted to an integer using the int() function.
    If the string can be converted to an integer, the function returns True.
    Otherwise, it returns False.

    Parameters:
        string (str): The input string that needs to be checked for validity

    Returns:
        bool: True if the input string can be converted to an integer, False otherwise
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def check_for_input():
    """
    This function prompts the user to enter an integer value
    for mass (in kg) and checks if the entered value is valid.
    If the entered value is valid, it is returned by the function.
    If the entered value is invalid, the function prints
    an error message and prompts the user to enter a valid integer value for mass.

    Returns:
        int: The valid integer value for mass entered by the user.
    """
    while True:
        user_input = input("Enter mass (in kg): ")

        if is_valid_int(user_input):
            mass = int(user_input)
            return mass
        else:
            print("Invalid input. Please enter an integer value for mass.")


main()
