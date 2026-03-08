data = [
    {"name": "Ata", "age": 30},
    {"name": "Ege", "age": 21},
    {"name": "Aysu", "age": 15},
    {"name": "İpek", "age": 19},
    {"name": "Ceren", "age": 20},
    {"name": "Alper", "age": 22},
]

filtered_list = [item for item in data if isinstance(item, dict) and (item['age'] > 20 or item['name'].startswith('A'))]

print(filtered_list)