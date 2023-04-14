def main():
    user_input = ''

    while ':)' not in user_input and ':(' not in user_input:
        user_input = input('Write something with :) or :( : ')

    print(convert(user_input))


def convert(string):
    string = string.replace(':)', '🙂')
    string = string.replace(':(', '🙁')
    return string


main()
