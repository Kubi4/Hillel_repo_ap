import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = requests.get(search_url, params=search_params)
if response.status_code == 200:
    data = response.json()
    items = data["collection"]["items"]
else:
    print('Помилка запиту:', response.status_code)

nasa_ids = []
for item in items:
    nasa_ids.append(item["data"][0]["nasa_id"])
    if len(nasa_ids) == 2:
        break

image_urls = []

for nasa_id in nasa_ids:
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    if response.status_code == 200:
        asset_data = asset_response.json()

        assets = asset_data["collection"]["items"]

        jpg_url = None
        for asset in assets:
            if asset["href"].endswith("~orig.jpg"):
                jpg_url = asset["href"]
                break
        if not jpg_url:
            for asset in assets:
                if asset["href"].endswith(".jpg"):
                    jpg_url = asset["href"]
                    break
        if jpg_url:
            image_urls.append(jpg_url)
    else:
        print('Помилка запиту:', response.status_code)

i = 1
for url in image_urls:
    img_response = requests.get(url)
    if response.status_code == 200:
        filename = f"mars_photo{i}.jpg"
        with open(filename, "wb") as f:
            f.write(img_response.content)
        i += 1
    else:
        print('Помилка запиту:', response.status_code)