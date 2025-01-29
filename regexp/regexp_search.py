import re

file_path = 'text.txt'

regex_patterns = {
    "Слова, заканчивающиеся на 'ing'": r'\b\w+ing\b',
    "Интервал дат": r'\b\d{4}-\d{4}\b',
    "Инициалы и фамилия": r'\b[A-Z]\.\s*[A-Z]\.\s*[A-Z][a-z]+\b',
}

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

for name, pattern in regex_patterns.items():
    matches = re.findall(pattern, text)
    print(f"Результаты для '{name}':")
    print("Первые 10 совпадений:", matches[:10])
    print("Общее количество совпадений:", len(matches))
    print("-" * 50)