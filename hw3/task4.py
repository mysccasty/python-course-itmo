# task4
import string


def file_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0
    longest_word = ""

    for line in lines:
        words = line.translate(str.maketrans('', '', string.punctuation)).split()
        word_count += len(words)
        char_count += len(line)

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

    return {
        'line_count': line_count,
        'word_count': word_count,
        'char_count': char_count,
        'longest_word': longest_word,
        'longest_word_length': len(longest_word)
    }


print(file_statistics('src/input.txt'))
