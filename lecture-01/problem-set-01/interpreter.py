x, y, z = input("Enter an aritmethic expression (e.g. 1 + 1): ").split()

x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
