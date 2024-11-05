#Binary Search

def word_to_weight(word):
    return sum(ord(char) for char in word)

def binary_search(weights, target_word):
    target_weight = word_to_weight(target_word)
    low, high = 0, len(weights) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_weight = weights[mid]
        print(mid_weight)

        if mid_weight == target_weight:
            return mid, mid_weight
        elif mid_weight < target_weight:
            low = mid + 1
        else:
            high = mid - 1


    return None

words = "girondists,potty,propylaeum,polyatomic,molluscous,scissors,unwish,corticated,fumbles,primates,horite,galeate,sorceresses"
words_dict = {}

for word in words.split(","):
    words_dict[word_to_weight(word)] = word
print(f"Данный словарь:\n{words_dict}")

words_dict = dict(sorted(words_dict.items()))
print(f"Отсортированный словарь:\n{words_dict}")
word_weights = list(words_dict.keys())
while True:
    search_word = input("Введите слово для поиска: ").strip()
    result = binary_search(word_weights, search_word)
    if result:
        index, weight = result
        print(f"Слово найдено: {search_word}")
        print(f"Вес слова: {weight}")
        print(f"Индекс слова в списке: {index}")
    else:
        print("Слово не найдено.")
