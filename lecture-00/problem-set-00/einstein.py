def main():
    mass = check_for_input()

    light_speed = 300000000
    energy = mass * light_speed ** 2

    print(f'The equivalent energy is {energy} Joules.')


def is_valid_int(string):
    """ check if the string can be converted to and integer """

    try:
        int(string)
        return True
    except ValueError:
        return False


def check_for_input():
    """ check if the input is valid. if not, the user will be prompted again """

    while True:
        user_input = input("Enter mass (in kg): ")

        if is_valid_int(user_input):
            mass = int(user_input)
            return mass
        else:
            print("Invalid input. Please enter an integer value for mass.")


main()
