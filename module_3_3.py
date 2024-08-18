def print_params(a=1, b=str, c = True):
    print(a, b, c)


print_params()
print_params(b=6, c={'one': 1})
print_params(c='str')

values_list = [True, 5.3, 'Hello']
values_dict = {'a': False, 'b': 5, 'c': 'Bye'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [{'One': 1}, True]

print_params(*values_list_2, 42)