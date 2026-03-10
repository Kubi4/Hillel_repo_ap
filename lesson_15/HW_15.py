import json
import logging
import os

logging.basicConfig(
    filename="json__Yakubenko.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder = "work_with_json"

for file_name in os.listdir(folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json.load(file)
            print(f"{file_path} — валідний JSON")
        except json.JSONDecodeError as e:
            logging.error(f"{file_path} — невалідний JSON: {e}")
            print(f"{file_path} — помилка JSON")
        except Exception as e:
            logging.error(f"{file_path} — помилка читання файлу: {e}")