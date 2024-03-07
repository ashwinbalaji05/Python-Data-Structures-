list_dicts = [{'a': 1, 'b': 3}, {'c': 5, 'd': 7}, {'e': 9, 'f': 11}]

tuple_list = [tuple(d.items()) for d in list_dicts]

print(tuple_list)

