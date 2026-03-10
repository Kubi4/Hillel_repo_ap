import json
import logging
import os
import csv
import xml.etree.ElementTree as ET

file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("json__Yakubenko.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

file_logger.addHandler(file_handler)


console_logger = logging.getLogger("console_logger")
console_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

console_logger.addHandler(console_handler)

"""завдання json"""

folder = "work_with_json"

for file_name in os.listdir(folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json.load(file)

        except json.JSONDecodeError as e:
            file_logger.error(f"{file_path} невалідний JSON: {e}")

        except Exception as e:
            file_logger.error(f"{file_path} помилка читання файлу: {e}")


"""завдання csv"""

csv_folder = "work_with_csv"

file1 = os.path.join(csv_folder, "random.csv")
file2 = os.path.join(csv_folder, "random-michaels.csv")

rows = []
seen = set()

for file_path in [file1, file2]:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            row_tuple = tuple(row)

            if row_tuple not in seen:
                seen.add(row_tuple)
                rows.append(row)

output_file = os.path.join(csv_folder, "result_Yakubenko.csv")

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)


"""завдання xml"""

xml_file = "work_with_xml/groups.xml"


def find_incoming_by_group_number(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")

            if number is not None and number.text == str(group_number):

                incoming = group.find("timingExbytes/incoming")

                if incoming is not None:
                    console_logger.info(
                        f"Group {group_number} incoming value: {incoming.text}"
                    )
                    return incoming.text

        console_logger.info(f"Group {group_number} not found")

    except Exception as e:
        console_logger.error(f"XML error: {e}")


find_incoming_by_group_number(xml_file, 1)