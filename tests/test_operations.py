from src.math_operations import (
    add, subtract, multiply, divide, power, modulus, floor_divide, 
    average, factorial, gcd, lcm, is_prime, fibonacci, sqrt, cube, 
    square, abs_value, round_number, max_in_list, min_in_list, 
    sum_of_list, product_of_list, variance, standard_deviation, 
    median, mode, permutation, combination, geometric_mean, 
    harmonic_mean, logarithm, exponential, sigmoid, tanh, cosine, 
    sine, tangent, cotangent, secant, cosecant
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Error: Division by zero"


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 2) == 100


def test_modulus():
    assert modulus(7, 3) == 1
    assert modulus(10, 5) == 0


def test_floor_divide():
    assert floor_divide(7, 3) == 2
    assert floor_divide(7, 0) == "Error: Division by zero"


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([]) == "Error: Empty list"


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Error: Negative number"


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5


def test_lcm():
    assert lcm(4, 5) == 20
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(4) == False
    assert is_prime(1) == False


def test_fibonacci():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [0]
    assert fibonacci(0) == "Error: Non-positive integer"


def test_sqrt():
    assert sqrt(16) == 4.0
    assert sqrt(-4) == "Error: Negative number"


def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0


def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0


def test_product_of_list():
    assert product_of_list([1, 2, 3, 4]) == 24
    assert product_of_list([]) == 1


def test_variance():
    assert variance([1, 2, 3, 4, 5]) == 2.0
    assert variance([]) == "Error: Empty list"


def test_standard_deviation():
    result = standard_deviation([1, 2, 3, 4, 5])
    assert abs(result - 1.4142135623730951) < 0.0001


def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([]) == "Error: Empty list"


def test_mode():
    assert mode([1, 2, 2, 3, 3, 3]) == [3]
    assert mode([1, 1, 2, 2]) == "No mode"
    assert mode([]) == "Error: Empty list"


def test_permutation():
    assert permutation(5, 3) == 60
    assert permutation(5, 0) == 1
    assert permutation(3, 5) == "Error: Invalid input"


def test_combination():
    assert combination(5, 3) == 10
    assert combination(5, 0) == 1
    assert combination(3, 5) == "Error: Invalid input"


def test_geometric_mean():
    assert geometric_mean([1, 3, 9]) == 3.0
    assert geometric_mean([]) == "Error: Empty list"


def test_harmonic_mean():
    assert harmonic_mean([1, 2, 4]) == 12 / 7
    assert harmonic_mean([]) == "Error: Invalid input"


def test_logarithm():
    assert logarithm(10, 10) == 1
    assert logarithm(100, 10) == 2
    assert logarithm(-10, 10) == "Error: Invalid input"


def test_exponential():
    import math
    assert exponential(1) == math.exp(1)
    assert exponential(0) == 1


def test_sigmoid():
    import math
    assert sigmoid(0) == 0.5
    result = sigmoid(1)
    expected = 1 / (1 + math.exp(-1))
    assert abs(result - expected) < 0.0001


def test_tanh():
    import math
    assert tanh(0) == 0
    assert abs(tanh(1) - math.tanh(1)) < 0.0001


def test_cosine():
    import math
    assert abs(cosine(0) - 1) < 0.0001
    assert abs(cosine(math.pi) - (-1)) < 0.0001


def test_sine():
    import math
    assert abs(sine(0)) < 0.0001
    assert abs(sine(math.pi / 2) - 1) < 0.0001


def test_tangent():
    import math
    assert abs(tangent(0)) < 0.0001
    assert abs(tangent(math.pi / 4) - 1) < 0.0001


def test_cotangent():
    import math
    assert abs(cotangent(math.pi / 4) - 1) < 0.0001


def test_secant():
    import math
    assert abs(secant(0) - 1) < 0.0001
    assert abs(secant(math.pi) - (-1)) < 0.0001


def test_cosecant():
    import math
    assert abs(cosecant(math.pi / 2) - 1) < 0.0001