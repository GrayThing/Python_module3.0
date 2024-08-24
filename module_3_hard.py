data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    res = 0
    for value in args:
        if isinstance(value, int):
            res += value
        if isinstance(value, str):
            res += len(value)
        if isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
            res += calculate_structure_sum(*value)
        if isinstance(value, dict):
            values_in_dict = list(value.items())
            res += calculate_structure_sum(*values_in_dict)
    return res


print(calculate_structure_sum(data_structure))


