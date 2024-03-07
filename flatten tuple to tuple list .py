def f_tuple_of_list(tuple_of_lists):
    f_list = []
    for s in tuple_of_lists:
        f_list += s
    return tuple(f_list)

# Example usage
tuple_of_lists = ([1, 2, 3], [4, 5,6], [7,8,9,10])
f_tuple = f_tuple_of_list(tuple_of_lists)
print(f_tuple)