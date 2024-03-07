tuple_list = [(1, 'b'), (3, 'a'), (2, 'c')]

n = 1  # Sort by the second element of each tuple

sorted_tuple_list = sorted(tuple_list, key=lambda x: x[n])

print(sorted_tuple_list)

