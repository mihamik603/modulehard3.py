def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple)):
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, str):
                    total_sum += len(key)
                total_sum += calculate_structure_sum([value])

    return total_sum



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) 