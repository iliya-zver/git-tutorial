# tuple = (1, 2, 3)
# hash_value = hash(tuple)
# print(hash_value)
# hash_value_2 = hash(tuple)
# print(hash_value_2)
# print(hash_value == hash_value_2)

def simple_hash(input_string):
    hash_value = 0
    for char in input_string:
        hash_value += ord(char)
    return hash_value

