# task3

def own_map(array, callback):
    return [callback(item) for item in array]


init_list = [1, 2, 3, 4, 5]
print(own_map(init_list, lambda x: x * 2))