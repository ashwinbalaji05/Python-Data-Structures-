def find_tuple_indices(tuples_to_find, tuple_list):
    return [i for i, tup in enumerate(tuple_list) if tup in tuples_to_find]

# Example usage:
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
tuples_to_find = [(3, 'c'), (5, 'e'), (6, 'f')]

indices = find_tuple_indices(tuples_to_find, tuple_list)
print("Indices of tuples to find:", indices)