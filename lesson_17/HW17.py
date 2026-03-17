# Генератори
# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n):
    for num in range(0, n + 1, 2):
        yield num

gen = even_numbers(17)

for x in gen:
    print(x)

# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

gen = fibonacci_generator_to(35)

for x in gen:
    print(x)

# Ітератори
# 1. Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

numbers = [10, 15, 20, 25, 30]

my_iterator = ReverseIterator(numbers)

for x in my_iterator:
    print(x)

# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 2
            return value
        else:
            raise StopIteration

even_iterator = EvenIterator(21)

for x in even_iterator:
    print(x)

# Декоратори
# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_generator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' Args: args={args}, kwargs={kwargs}")
        for value in func(*args, **kwargs):
            print(f"Generator '{func.__name__}' result: {value}")
            yield value
    return wrapper

@log_generator
def even_numbers(n):
    for num in range(0, n + 1, 2):
        yield num

gen = even_numbers(17)

for x in gen:
    print(f"Result: {x}")

# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            for value in func(*args, **kwargs):
                yield value
        except Exception as e:
            print(f"Exception in '{func.__name__}': {type(e).__name__} - {e}")
    return wrapper

@catch_exceptions
def fibonacci_generator_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

gen = fibonacci_generator_to("t")

for x in gen:
    print(x)