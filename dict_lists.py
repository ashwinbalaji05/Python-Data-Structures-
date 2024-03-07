dict_with_lists = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

dict_list = [{key: value[i] for key, value in dict_with_lists.items()} for i in range(len(next(iter(dict_with_lists.values()))))]

print(dict_list)


