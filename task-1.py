import json
def calculate_weighted_score(filename):
    # Открываем и читаем JSON файл
    with open(filename, 'r') as file:
        input = json.load(file)

    # Вычисляем сумму произведений score и weight
    total_sum = sum(item['score'] * item['weight'] for item in input)

    # Округляем результат до 3 знаков после запятой и возвращаем
    return round(total_sum, 3)
result = calculate_weighted_score('input.json')
print(result)
