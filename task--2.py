# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Список для хранения данных
    data = []

    # Чтение CSV файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Преобразование каждой строки в словарь и добавление в список
        for row in csv_reader:
            data.append(row)

    # Запись данных в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
