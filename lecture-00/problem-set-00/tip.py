def main():
    """
    Calculates the tip amount for a meal based on the cost and the desired tip percentage.
    """

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_string):
    """
    Converts a dollar amount represented as a string to a floating-point number.

    Args:
        dollar_string (str): A string representation of a dollar amount,
        including the dollar sign ($).

    Returns:
        float: The floating-point representation of the dollar amount,
        obtained by removing the dollar sign from the input string
        and converting the resulting string to a float.
    """

    without_dollar_sign = dollar_string.replace("$", "")
    return float(without_dollar_sign)


def percent_to_float(percentage_string):
    """
    Converts a percentage represented as a string to a floating-point number.

    Args:
        percentage_string (str): A string representation of a percentage,
        including the percentage sign (%).

    Returns:
        float: The floating-point representation of the percentage,
        obtained by removing the percentage sign from the input string,
        converting the resulting string to a float, and dividing the result by 100.
    """

    without_percentage_sign = percentage_string.replace("%", "")
    return float(without_percentage_sign) / 100


main()
