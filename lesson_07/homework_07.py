# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_2_numbers(a, b):
    return a + b
print(sum_of_2_numbers(3, 7))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(list_numbers_t2):
    return sum(list_numbers_t2)/len(list_numbers_t2)
print(arithmetic_mean([1, 2, 3, 4]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(str_t4):
    return str_t4[::-1]
print(reverse_string("Test"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(list_words_t5):
    return max(list_words_t5, key=len)
print(longest_word(["Test", "Function", "Verification", "Pagination"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def pc_price(monthly_payment, all_months):
    return monthly_payment * all_months

print(pc_price(1179, all_months=18))

# task 8
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274
pizza_medium = 218
juice = 35
cake = 350
water = 21
def order_price(order_dict):
    full_price = 0
    for key, value in order_dict.items():
        item_price = key*value
        full_price += item_price
    return full_price
print(order_price({pizza_big: 4, pizza_medium: 2, juice: 4, cake : 1, water: 3}))

# task 9
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def pages_quantity(all_photos, max_photos_per_page):
    return all_photos // max_photos_per_page
print(pages_quantity(232, 8))
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# distance = 1600
# fuel_for_100_km = 9
# fuel_tank = 48
# fuel_for_trip = distance // 100 * fuel_for_100_km
# gas_stops = fuel_for_trip // fuel_tank

def fuel_and_stops(distance, fuel_for_100_km, fuel_tank):
    fuel_for_trip = distance // 100 * fuel_for_100_km
    gas_stops = fuel_for_trip // fuel_tank
    result_dict = {"Fuel for trip": fuel_for_trip, "Gas stops": gas_stops}
    return result_dict
print(fuel_and_stops(1600, 9, 48))

