import math
from math import *

constants = ["pi", "e"]
non_includes = ["^", "!", "%"]
trigonometrics = ["sin", "cos", "tan", "cot", "sec", "csc"]


# Check if a value is an integer, and if it is an integer, return True; else, return False
def is_int(x):
    if x[0] in ('-', '+'):
        return x[1:].isdigit()
    return x.isdigit()


# Returns the integer value of something if its integer, else ask to user again
def get_int(_boolen, x, something):
    x = input(something)
    while not is_int(x) and _boolen:
        x = input(something)
        if is_int(x):
            _boolen = False
    return int(x)


# Option1 that solves equations
def option1():
    print()
    print("---------Equation Solver----------")
    print()
    print(f"1- I. Degree Equation\n"
          f"2- II. Degree Equation\n")
    boolen1 = True
    x = None
    x = get_int(boolen1, x, "Please choose the degree of equation : ")

    if not (3 > x > 0):
        x = input("Please choose the degree of equation : ")
    else:
        if x == 1:
            print("For equation ax+b = 0 enter the a and b.")
            _boolen1 = True
            _boolen2 = True
            a = None
            b = None
            a = get_int(_boolen1, a, "a : ")
            b = get_int(_boolen1, b, "b : ")
            fx = -b / a
            print(f"For values a = {a}, b = {b} :\nx = {fx}")
        elif x == 2:
            print("For equation ax^2+bx+c = 0 enter a,b and c.")
            _boolen1 = True
            _boolen2 = True
            _boolen3 = True
            a = None
            b = None
            c = None
            a = get_int(_boolen1, a, "a : ")
            b = get_int(_boolen1, b, "b : ")
            c = get_int(_boolen1, c, "c : ")
            delta = (b * b) - (4 * a * c)
            if delta >= 0:
                fx1 = (-b - math.pow(delta, .5)) / (2 * a)
                fx2 = (-b + math.pow(delta, .5)) / (2 * a)
                print(f"For values a = {a}, b = {b}, c = {c} :\nx1 = {fx1}\nx2 = {fx2}")
            else:
                print(f"For values a = {a}, b = {b}, c = {c} :\n There are no reel roots!")


# Option 2 left to right calculator
def option2():
    print()
    print("---------Calculator----------")
    print()

    process = str(input("Please enter the value to be calculated : "))

    result = None

    left = "left"
    right = "right"

    def find_number(x, side, _input):
        left_numbers = []
        right_numbers = []
        length_of_x = len(x)

        if side == "left":
            x_queue = _input.find(x)

            while x_queue > 0 and (_input[x_queue - 1].isdigit() or _input[x_queue - 1] == "."):
                x_queue = x_queue - 1
                left_numbers.append(_input[x_queue])

            left_numbers.reverse()

            final_string = ""
            for i in range(len(left_numbers)):
                final_string = final_string + left_numbers[i]

            return str(final_string)
        elif side == "right":
            x_queue = _input.find(x)
            while x_queue + length_of_x < len(_input) and (
                    _input[x_queue + length_of_x].isdigit() or _input[x_queue + length_of_x] == "."):
                right_numbers.append(_input[x_queue + length_of_x])
                x_queue += 1

                final_string = ""
                for i in range(len(right_numbers)):
                    final_string = final_string + right_numbers[i]
            return str(final_string)
        else:
            print("Something went wrong!")

    def trigonoms(function, number):
        if function == "sin":
            return float(math.sin(number))
        elif function == "cos":
            return float(math.cos(number))
        elif function == "tan":
            return float(math.tan(number))
        elif function == "cot":
            return float(1 / math.tan(number))
        elif function == "sec":
            return float(1 / math.cos(number))
        elif function == "csc":
            return float(1 / math.sin(number))

    def reduce_layer(_process):
        _process = _process.strip()

        # ------------Constansts-------------- #
        if _process.count("pi") >= 1:
            _process = _process.replace("pi", f"{math.pi}", _process.count("pi"))
        if _process.count("e") >= 1:
            _process = _process.replace("e", f"{math.e}", _process.count("e"))

        # ------------Non_Includes------------ #
        while _process.count("^") > 0:
            left_number = find_number("^", left, _process)
            right_number = find_number("^", right, _process)

            if left_number.count(".") >= 1:
                left_number = float(left_number)
            else:
                left_number = int(left_number)
            if right_number.count(".") >= 1:
                right_number = float(right_number)
            else:
                right_number = int(right_number)

            _process = _process.replace(str(f'{str(left_number)}^{str(right_number)}'),
                                        str(float(math.pow(left_number, right_number))), 1)

        while _process.count("!") > 0:
            try:
                left_number = find_number("!", left, _process)
                if left_number.count(".") >= 1:
                    left_number = float(left_number)
                else:
                    left_number = int(left_number)
                _process = _process.replace(str(f"{str(left_number)}!"), str(float(math.factorial(left_number))), 1)
            except:
                print("The factorial operator takes only integer values! ( Example Usage : 4! )")
                break

        while _process.count("%") > 0:
            left_number = find_number("%", left, _process)
            if left_number.count(".") >= 1:
                left_number = float(left_number)
            else:
                left_number = int(left_number)
            _process = _process.replace(str(f"{str(left_number)}%"), str(float(left_number / 100)), 1)

        # -----------Trigonometrics---------- #
        for i in range(len(trigonometrics)):
            func = trigonometrics[i]
            while _process.count(f"{func}(") > 0:
                right_number = find_number(f"{func}(", right, _process)
                if right_number.count(".") >= 1:
                    right_number = float(right_number)
                else:
                    right_number = int(right_number)
                _process = _process.replace(str(f"{func}({right_number})"), str(trigonoms(func, right_number)), 1)

        return _process

    result = reduce_layer(process)

    print(eval(str(result)))


# Final loop that asks to player if player wants to make a new operation or not
calculator = True
while calculator:
    print(f"1- Equation Solver")
    print(f"2- Calculator")
    print()
    inpt = input("Please select the operation that you want to do: ")

    boolen4 = True
    while boolen4:
        if inpt == "1":
            try:
                option1()
                if inpt == "1":
                    boolen4 = False
            except:
                None
        elif inpt == "2":
            option2()
            if inpt == "2":
                boolen4 = False
        else:
            inpt = input("Please select the operation that you want to do ( Options are just 1 and 2 ) : ")
    loop = True
    while loop:
        print()
        yes_no = input("Would you like to make a new operation? Yes: y / No: n ")
        if yes_no == "y":
            loop = False
            calculator = True
        elif yes_no == "n":
            loop = False
            calculator = False
            print("Application Closed!")
        else:
            loop = True
