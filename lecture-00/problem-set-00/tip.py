def main():
    """
    Prompts the user for the meal cost and the tip percentage.

    Calculates the tip amount, and displays it.
    """

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_string):
    """
    It takes a string argument 'dollar_string', which represents the meal cost in dollars, and converts it to a floating point number.

    Removes the '$' sign from the string before converting it to a float.
    """

    without_dollar_sign = dollar_string.replace("$", "")
    return float(without_dollar_sign)


def percent_to_float(percentage_string):
    """
    It  takes a string argument 'percentage_string', which represents the tip percentage, and converts it to a floating point number.

    Removes the '%' sign from the string and divides the resulting number by 100 to get the percentage in decimal form.
    """

    without_percentage_sign = percentage_string.replace("%", "")
    return float(without_percentage_sign) / 100


main()
