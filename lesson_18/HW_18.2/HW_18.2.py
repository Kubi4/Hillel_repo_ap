import requests

BASE_URL = 'http://127.0.0.1:8080'

image_path = 'mountain.jpg'  # шлях до зображення на твоєму комп'ютері
with open(image_path, 'rb') as f:
    files = {'image': f}
    response = requests.post(f'{BASE_URL}/upload', files=files)

if response.status_code == 201:
    data = response.json()
    image_url = data['image_url']
    print('Завантажено зображення:', image_url)
else:
    print('Помилка завантаження:', response.text)
    exit()

filename = image_path.split('/')[-1]

headers = {'Content-Type': 'text'}
response = requests.get(f'{BASE_URL}/image/{filename}', headers=headers)
if response.status_code == 200:
    print('Отримано URL зображення:', response.json()['image_url'])
else:
    print('Помилка отримання зображення:', response.text)

response = requests.delete(f'{BASE_URL}/delete/{filename}')
if response.status_code == 200:
    print('Зображення видалено:', response.json()['message'])
else:
    print('Помилка видалення зображення:', response.text)