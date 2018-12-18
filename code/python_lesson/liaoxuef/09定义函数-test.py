import math

def quadratic(a, b, c):
    my_number = b * b - 4 * a * c
    my_number1 = math.sqrt(my_number)
    my_ans1 = ((-b) + my_number1)/(2*a)
    my_ans2 = ((-b) - my_number1)/(2*a)
    if my_number > 0:
        return my_ans1, my_ans2
    else:
        if my_number == 0:
            return -b/(2*a)
        else:
            return None

print(quadratic(2, 3, 1))

print("\n")

print(quadratic(1, 3, -4))


