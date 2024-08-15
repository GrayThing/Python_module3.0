calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    new_tuple = (len(string), string.upper(), string.lower())
    return new_tuple


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for value in list_to_search:
        if value.lower() == string.lower():
            flag = True
    return flag


print(string_info('Worldwide'))
print(string_info('Poetry'))
print(is_contains('Hyper', ['PC', 'FuN', 'hyPer']))
print(is_contains('Black', ['white', 'YeLlow']))
print(is_contains('watch', ['seE', 'LooK', 'wAtcH']))
print(calls)
