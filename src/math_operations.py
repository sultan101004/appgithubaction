def add(a,b) : 
    return a + b

def subtract(a,b) :
    return a - b

def multiply(a,b) :
    return a * b

def divide(a,b) :
    if b == 0 :
        return "Error: Division by zero"
    return a / b

def power(a,b) :
    return a ** b

def modulus(a,b) :
    return a % b

def floor_divide(a,b) :
    if b == 0 :
        return "Error: Division by zero"
    return a // b

def average(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    return sum(numbers) / len(numbers)

def factorial(n) :
    if n < 0 :
        return "Error: Negative number"
    if n == 0 or n == 1 :
        return 1
    result = 1
    for i in range(2, n + 1) :
        result *= i
    return result

def gcd(a,b) :
    while b :
        a, b = b, a % b
    return a

def lcm(a,b) :
    if a == 0 or b == 0 :
        return 0
    return abs(a * b) // gcd(a, b)

def is_prime(n) :
    if n <= 1 :
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def fibonacci(n) :
    if n <= 0 :
        return "Error: Non-positive integer"
    fib_sequence = [0, 1]
    for i in range(2, n) :
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def sqrt(n) :
    if n < 0 :
        return "Error: Negative number"
    return n ** 0.5

def cube(n) :
    return n ** 3

def square(n) :
    return n ** 2

def abs_value(n) :
    return abs(n)

def round_number(n, digits=0) :
    return round(n, digits)

def max_in_list(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    return max(numbers)

def min_in_list(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    return min(numbers)

def sum_of_list(numbers) :
    return sum(numbers)

def product_of_list(numbers) :
    result = 1
    for num in numbers :
        result *= num
    return result

def variance(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    mean = average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    return variance(numbers) ** 0.5

def median(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0 :
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else :
        return sorted_numbers[mid]
    
def mode(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    frequency = {}
    for num in numbers :
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    if len(modes) == len(frequency) :
        return "No mode"
    return modes

def percentile(numbers, percent) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    index = int((n - 1) * percent)
    return sorted_numbers[index]

def z_score(numbers, x) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    mean = average(numbers)
    std_dev = standard_deviation(numbers)
    if std_dev == 0 :
        return "Error: Standard deviation is zero"
    return (x - mean) / std_dev

def linear_regression(x, y) :
    if len(x) != len(y) or len(x) == 0 :
        return "Error: Invalid input"
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

def quadratic_formula(a, b, c) :
    if a == 0 :
        return "Error: Not a quadratic equation"
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 :
        return "Error: No real roots"
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return root1, root2

def permutation(n, r) :
    if r > n or n < 0 or r < 0 :
        return "Error: Invalid input"
    return factorial(n) // factorial(n - r)

def combination(n, r) :
    if r > n or n < 0 or r < 0 :
        return "Error: Invalid input"
    return factorial(n) // (factorial(r) * factorial(n - r))

def geometric_mean(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    product = product_of_list(numbers)
    return product ** (1 / len(numbers))

def harmonic_mean(numbers) :
    if len(numbers) == 0 or any(num == 0 for num in numbers) :
        return "Error: Invalid input"
    return len(numbers) / sum(1 / num for num in numbers)

def logarithm(n, base=10) :
    if n <= 0 or base <= 1 :
        return "Error: Invalid input"
    import math
    return math.log(n, base)

def exponential(n) :
    import math
    return math.exp(n)

def sigmoid(x) :
    import math
    return 1 / (1 + math.exp(-x))

def tanh(x) :
    import math
    return math.tanh(x)

def cosine(x) :
    import math
    return math.cos(x)

def sine(x) :
    import math
    return math.sin(x)

def tangent(x) :
    import math
    return math.tan(x)

def cotangent(x) :
    import math
    return 1 / math.tan(x)

def secant(x) :
    import math
    return 1 / math.cos(x)  

def cosecant(x) :
    import math
    return 1 / math.sin(x)

def degrees_to_radians(deg) :
    import math
    return deg * (math.pi / 180)

def radians_to_degrees(rad) :
    import math
    return rad * (180 / math.pi)

def mean_absolute_deviation(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    mean = average(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def interquartile_range(numbers) :
    if len(numbers) == 0 :
        return "Error: Empty list"
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    q1 = median(sorted_numbers[:n//2])
    q3 = median(sorted_numbers[(n+1)//2:])
    return q3 - q1

def covariance(x, y) :
    if len(x) != len(y) or len(x) == 0 :
        return "Error: Invalid input"
    mean_x = average(x)
    mean_y = average(y)
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / len(x)

def correlation_coefficient(x, y) :
    if len(x) != len(y) or len(x) == 0 :
        return "Error: Invalid input"
    cov = covariance(x, y)
    std_dev_x = standard_deviation(x)
    std_dev_y = standard_deviation(y)
    if std_dev_x == 0 or std_dev_y == 0 :
        return "Error: Standard deviation is zero"
    return cov / (std_dev_x * std_dev_y)

def linear_interpolation(x0, y0, x1, y1, x) :
    if x1 - x0 == 0 :
        return "Error: Division by zero"
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def quadratic_interpolation(x0, y0, x1, y1, x2, y2, x) :
    if x1 - x0 == 0 or x2 - x0 == 0 or x2 - x1 == 0 :
        return "Error: Division by zero"
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0) + (y2 - y0) * (x - x0) * (x - x1) / ((x2 - x0) * (x1 - x0))

def cubic_interpolation(x0, y0, x1, y1, x2, y2, x3, y3, x) :
    if x1 - x0 == 0 or x2 - x0 == 0 or x3 - x0 == 0 or x2 - x1 == 0 or x3 - x1 == 0 or x3 - x2 == 0 :
        return "Error: Division by zero"
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0) + (y2 - y0) * (x - x0) * (x - x1) / ((x2 - x0) * (x1 - x0)) + (y3 - y0) * (x - x0) * (x - x1) * (x - x2) / ((x3 - x0) * (x2 - x0) * (x3 - x1))

def trapezoidal_rule(f, a, b, n) :
    if n <= 0 or a >= b :
        return "Error: Invalid input"
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n) :
        integral += f(a + i * h)
    integral *= h
    return integral

def simpsons_rule(f, a, b, n) :
    if n <= 0 or n % 2 != 0 or a >= b :
        return "Error: Invalid input"
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2) :
        integral += 4 * f(a + i * h)
    for i in range(2, n-1, 2) :
        integral += 2 * f(a + i * h)
    integral *= h / 3
    return integral

def euler_method(f, y0, t0, t_end, h) :
    if h <= 0 or t0 >= t_end :
        return "Error: Invalid input"
    n = int((t_end - t0) / h)
    t = t0
    y = y0
    results = [(t, y)]
    for i in range(n) :
        y += h * f(t, y)
        t += h
        results.append((t, y))
    return results

def runge_kutta_4th_order(f, y0, t0, t_end, h) :
    if h <= 0 or t0 >= t_end :
        return "Error: Invalid input"
    n = int((t_end - t0) / h)
    t = t0
    y = y0
    results = [(t, y)]
    for i in range(n) :
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        results.append((t, y))
    return results


