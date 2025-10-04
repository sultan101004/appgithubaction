from src.math_operations import add, subtract, multiply, divide, permutation, combination, geometric_mean, harmonic_mean, logarithm, exponential, sigmoid, tanh, cosine, sine, tangent, cotangent, secant, cosecant, factorial, product_of_list, gcd, lcm, is_prime, prime_factors, fibonacci, fibonacci_nth, is_palindrome, is_armstrong, is_perfect, collatz_sequence, sum_of_squares, square_of_sum, mean, median, mode, variance, standard_deviation, average, floor_divide, modulus, sqrt, cube


def test_add() :
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract() :
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply() :
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide() :
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Error: Division by zero"

def test_permutation() :
    assert permutation(5, 3) == 60
    assert permutation(5, 0) == 1
    assert permutation(3, 5) == "Error: Invalid input"

def test_combination() :
    assert combination(5, 3) == 10
    assert combination(5, 0) == 1
    assert combination(3, 5) == "Error: Invalid input"

def test_geometric_mean() :
    assert geometric_mean([1, 3, 9]) == 3.0
    assert geometric_mean([]) == "Error: Empty list"

def test_harmonic_mean() :
    assert harmonic_mean([1, 2, 4]) == 12 / 7
    assert harmonic_mean([]) == "Error: Invalid input"
    assert harmonic_mean([1, 0, 4]) == "Error: Invalid input"

def test_logarithm() :
    assert logarithm(10, 10) == 1
    assert logarithm(100, 10) == 2

    assert logarithm(-10, 10) == "Error: Invalid input"

    assert logarithm(10, 1) == "Error: Invalid input"

def test_exponential() :
    import math
    assert exponential(1) == math.exp(1)
    assert exponential(0) == 1
    assert exponential(-1) == math.exp(-1)

def test_sigmoid() :
    import math
    assert sigmoid(0) == 0.5
    assert sigmoid(1) == 1 / (1 + math.exp(-1))
    assert sigmoid(-1) == 1 / (1 + math.exp(1))

def test_tanh() :
    import math
    assert tanh(0) == 0
    assert tanh(1) == math.tanh(1)
    assert tanh(-1) == math.tanh(-1)

def test_cosine() :
    import math
    assert cosine(0) == 1
    assert cosine(math.pi / 2) == 0
    assert cosine(math.pi) == -1
    assert cosine(3 * math.pi / 2) == 0
    assert cosine(2 * math.pi) == 1
    assert cosine(math.pi / 4) == math.sqrt(2) / 2
    assert cosine(-math.pi / 4) == math.sqrt(2) / 2
    assert cosine(3 * math.pi / 4) == -math.sqrt(2) / 2
    assert cosine(-3 * math.pi / 4) == -math.sqrt(2) / 2

def test_sine() :
    import math
    assert sine(0) == 0
    assert sine(math.pi / 2) == 1
    assert sine(math.pi) == 0
    assert sine(3 * math.pi / 2) == -1
    assert sine(2 * math.pi) == 0
    assert sine(math.pi / 4) == math.sqrt(2) / 2
    assert sine(-math.pi / 4) == -math.sqrt(2) / 2
    assert sine(3 * math.pi / 4) == math.sqrt(2) / 2
    assert sine(-3 * math.pi / 4) == -math.sqrt(2) / 2

def test_tangent() :
    import math
    assert tangent(0) == 0
    assert tangent(math.pi / 2) == 1
    assert tangent(math.pi) == -1
    assert tangent(3 * math.pi / 2) == -1
    assert tangent(2 * math.pi) == 1
    assert tangent(math.pi / 4) == 1
    assert tangent(-math.pi / 4) == -1
    assert tangent(3 * math.pi / 4) == -1
    assert tangent(-3 * math.pi / 4) == 1

def test_cotangent() :
    import math
    assert cotangent(math.pi / 4) == 1
    assert cotangent(-math.pi / 4) == -1
    assert cotangent(3 * math.pi / 4) == -1
    assert cotangent(-3 * math.pi / 4) == 1
    assert cotangent(math.pi / 2) == 0
    assert cotangent(3 * math.pi / 2) == 0

def test_secant() :
    import math
    assert secant(0) == 1
    assert secant(math.pi) == -1
    assert secant(2 * math.pi) == 1
    assert secant(math.pi / 4) == math.sqrt(2)
    assert secant(-math.pi / 4) == math.sqrt(2)
    assert secant(3 * math.pi / 4) == -math.sqrt(2)
    assert secant(-3 * math.pi / 4) == -math.sqrt(2)
    assert secant(math.pi / 2) == "Error: Undefined"
    assert secant(3 * math.pi / 2) == "Error: Undefined"
    assert secant(math.pi / 3) == 2
    assert secant(-math.pi / 3) == 2
    assert secant(2 * math.pi / 3) == -2
    assert secant(-2 * math.pi / 3) == -2
    assert secant(math.pi / 6) == 2 / math.sqrt(3)
    assert secant(-math.pi / 6) == 2 / math.sqrt(3)
    assert secant(5 * math.pi / 6) == -2 / math.sqrt(3)
    assert secant(-5 * math.pi / 6) == -2 / math.sqrt(3)
    assert secant(math.pi / 12) == 2 / (math.sqrt(6) + math.sqrt(2))
    assert secant(-math.pi / 12) == 2 / (math.sqrt(6) + math.sqrt(2))
    assert secant(11 * math.pi / 12) == -2 / (math.sqrt(6) + math.sqrt(2))
    assert secant(-11 * math.pi / 12) == -2 / (math.sqrt(6) + math.sqrt(2))
    assert secant(math.pi / 8) == math.sqrt(2 + math.sqrt(2))
    assert secant(-math.pi / 8) == math.sqrt(2 + math.sqrt(2))
    assert secant(7 * math.pi / 8) == -math.sqrt(2 + math.sqrt(2))
    assert secant(-7 * math.pi / 8) == -math.sqrt(2 + math.sqrt(2))
    assert secant(3 * math.pi / 8) == math.sqrt(2 - math.sqrt(2))
    assert secant(-3 * math.pi / 8) == math.sqrt(2 - math.sqrt(2))
    assert secant(5 * math.pi / 8) == -math.sqrt(2 - math.sqrt(2))
    assert secant(-5 * math.pi / 8) == -math.sqrt(2 - math.sqrt(2))
    assert secant(math.pi / 5) == (math.sqrt(5) + 1) / 2
    assert secant(-math.pi / 5) == (math.sqrt(5) + 1) / 2
    assert secant(4 * math.pi / 5) == -(math.sqrt(5) + 1) / 2
    assert secant(-4 * math.pi / 5) == -(math.sqrt(5) + 1) / 2
    assert secant(2 * math.pi / 5) == (math.sqrt(5) - 1) / 2
    assert secant(-2 * math.pi / 5) == (math.sqrt(5) - 1) / 2
    assert secant(3 * math.pi / 5) == -(math.sqrt(5) - 1) / 2
    assert secant(-3 * math.pi / 5) == -(math.sqrt(5) - 1) / 2
    assert secant(math.pi / 10) == 4 / (math.sqrt(5) + 1)
    assert secant(-math.pi / 10) == 4 / (math.sqrt(5) + 1)
    assert secant(9 * math.pi / 10) == -4 / (math.sqrt(5) + 1)
    assert secant(-9 * math.pi / 10) == -4 / (math.sqrt(5) + 1)
    assert secant(3 * math.pi / 10) == 4 / (math.sqrt(5) - 1)
    assert secant(-3 * math.pi / 10) == 4 / (math.sqrt(5) - 1)
    assert secant(7 * math.pi / 10) == -4 / (math.sqrt(5) - 1)
    assert secant(-7 * math.pi / 10) == -4 / (math.sqrt(5) - 1)
    assert secant(math.pi / 20) == math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(-math.pi / 20) == math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(19 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(-19 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(3 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert secant(-3 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert secant(17 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(-17 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert secant(5 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert secant(-5 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert secant(15 * math.pi / 20) == -math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert secant(-15 * math.pi / 20) == -math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))

def test_cosecant() :
    import math
    assert cosecant(math.pi / 2) == 1
    assert cosecant(3 * math.pi / 2) == -1
    assert cosecant(math.pi / 4) == math.sqrt(2)
    assert cosecant(-math.pi / 4) == -math.sqrt(2)
    assert cosecant(3 * math.pi / 4) == math.sqrt(2)

    assert cosecant(-3 * math.pi / 4) == -math.sqrt(2)
    assert cosecant(math.pi / 6) == 2
    assert cosecant(-math.pi / 6) == -2
    assert cosecant(5 * math.pi / 6) == 2
    assert cosecant(-5 * math.pi / 6) == -2
    assert cosecant(math.pi / 3) == 2 / math.sqrt(3)
    assert cosecant(-math.pi / 3) == -2 / math.sqrt(3)
    assert cosecant(2 * math.pi / 3) == 2 / math.sqrt(3)
    assert cosecant(-2 * math.pi / 3) == -2 / math.sqrt
    assert cosecant(math.pi / 12) == 4 / (math.sqrt(6) - math.sqrt(2))
    assert cosecant(-math.pi / 12) == -4 / (math.sqrt(6) - math.sqrt(2))
    assert cosecant(11 * math.pi / 12) == 4 / (math.sqrt(6) + math.sqrt(2))
    assert cosecant(-11 * math.pi / 12) == -4 / (math.sqrt(6) + math.sqrt(2))
    assert cosecant(math.pi / 8) == math.sqrt(2) * math.sqrt(2 + math.sqrt(2))
    assert cosecant(-math.pi / 8) == -math.sqrt(2) * math.sqrt(2 + math.sqrt(2))
    assert cosecant(7 * math.pi / 8) == math.sqrt(2) * math.sqrt(2 + math.sqrt(2))
    assert cosecant(-7 * math.pi / 8) == -math.sqrt(2) * math.sqrt(2 + math.sqrt(2))
    assert cosecant(3 * math.pi / 8) == math.sqrt(2) * math.sqrt(2 - math.sqrt(2))
    assert cosecant(-3 * math.pi / 8) == -math.sqrt(2) * math.sqrt(2 - math.sqrt(2))
    assert cosecant(5 * math.pi / 8) == math.sqrt(2)
    assert cosecant(-5 * math.pi / 8) == -math.sqrt(2) * math.sqrt(2 - math.sqrt(2))
    assert cosecant(math.pi / 5) == (math.sqrt(5) + 1) / (math.sqrt(5) - 1)
    assert cosecant(-math.pi / 5) == -(math.sqrt(5) + 1) / (math.sqrt(5) - 1)
    assert cosecant(4 * math.pi / 5) == (math.sqrt(5) + 1) / (math.sqrt(5) - 1)
    assert cosecant(-4 * math.pi / 5) == -(math.sqrt(5) + 1) / (math.sqrt(5) - 1)
    assert cosecant(2 * math.pi / 5) == (math.sqrt(5) - 1) / 2
    assert cosecant(-2 * math.pi / 5) == -(math.sqrt(5) - 1) / 2
    assert cosecant(3 * math.pi / 5) == (math.sqrt(5) - 1) / 2
    assert cosecant(-3 * math.pi / 5) == -(math.sqrt(5) - 1) / 2
    assert cosecant(math.pi / 10) == 4 / math.sqrt(10 - 2 * math.sqrt(5))
    assert cosecant(-math.pi / 10) == -4 / math.sqrt(10 - 2 * math.sqrt(5))
    assert cosecant(9 * math.pi / 10) == 4 / math.sqrt(10 + 2 * math.sqrt(5))
    assert cosecant(-9 * math.pi / 10) == -4 / math.sqrt(10 + 2 * math.sqrt(5))
    assert cosecant(math.pi / 20) == math.sqrt(10 + 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(-math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(19 * math.pi / 20) == math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(-19 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(3 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(-3 * math.pi / 20) == -math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(17 * math.pi / 20) == math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(-17 * math.pi / 20) == -math.sqrt(10 + 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 + math.sqrt(5)))
    assert cosecant(5 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(-5 * math.pi / 20) == -math.sqrt(10 - 2 * math.sqrt(5) + 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(15 * math.pi / 20) == math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(-15 * math.pi / 20) == -math.sqrt(10 - 2 * math.sqrt(5) - 2 * math.sqrt(2) * math.sqrt(5 - math.sqrt(5)))
    assert cosecant(0) == "Error: Undefined"
    assert cosecant(math.pi) == "Error: Undefined"
    assert cosecant(2 * math.pi) == "Error: Undefined"
    assert cosecant(4 * math.pi) == "Error: Undefined"
    assert cosecant(-math.pi) == "Error: Undefined"
    assert cosecant(-2 * math.pi) == "Error: Undefined"
    assert cosecant(-4 * math.pi) == "Error: Undefined"
    assert cosecant(6 * math.pi) == "Error: Undefined"
    assert cosecant(-6 * math.pi) == "Error: Undefined"


def test_factorial() :
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Error: Negative input"

def test_gcd() :
    assert gcd(48, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_lcm() :
    assert lcm(4, 5) == 20
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    assert lcm(0, 0) == 0

def test_is_prime() :
    assert is_prime(7) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    assert is_prime(-3) == False

def test_fibonacci() :
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [0]
    assert fibonacci(0) == "Error: Non-positive integer"
    assert fibonacci(-5) == "Error: Non-positive integer"

def test_average() :
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([]) == "Error: Empty list"

def test_product_of_list() :
    assert product_of_list([1, 2, 3, 4]) == 24
    assert product_of_list([]) == 1

def test_divide_integer() :
    assert floor_divide(7, 3) == 2
    assert floor_divide(7, 0) == "Error: Division by zero"

def test_modulus() :
    assert modulus(7, 3) == 1
    assert modulus(7, 0) == "Error: Division by zero"

def test_sqrt() :
    assert sqrt(16) == 4.0
    assert sqrt(-4) == "Error: Negative number"


def test_cube() :
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0



# Additional tests can be added for other functions as needed


