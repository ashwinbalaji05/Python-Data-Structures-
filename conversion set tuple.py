def set_to_tuple(set_input):
    return tuple(set_input)

def tuple_to_set(tuple_input):
    return set(tuple_input)

# Example usage
set_input = {2,4,6,8,10}
converted_tuple = set_to_tuple(set_input)
print("Set converted to tuple:", converted_tuple)

tuple_input = (1,3,5,7,9)
converted_set = tuple_to_set(tuple_input)
print("Tuple converted to set:", converted_set)


