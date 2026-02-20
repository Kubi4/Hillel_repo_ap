#Функція 1
""" Написати функцію, яка обчислює суму двох чисел """

def sum_of_2_numbers(a, b):
    return a + b

#Функція 2
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку """

def reverse_string(str):
    return str[::-1]

#Функція 3
""" Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення """

def order_price(order_dict):
    full_price = 0
    for key, value in order_dict.items():
        item_price = key*value
        full_price += item_price
    return full_price

#Функція 4
""" Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото? """

def pages_quantity(all_photos, max_photos_per_page):
    return (all_photos + max_photos_per_page - 1) // max_photos_per_page
