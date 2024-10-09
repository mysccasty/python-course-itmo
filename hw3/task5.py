# task5
def merge_files(file_paths, write_to_file=True):
    result = ""
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            result += file.read()
    if write_to_file:
        with open('src/merged_file.txt', 'w') as file:
            file.write(result)
    return result


print(merge_files(['src/input.txt', 'src/input1.txt', 'src/input2.txt']))
