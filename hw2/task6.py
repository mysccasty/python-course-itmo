#task6
import string
from collections import Counter

s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."
print(f"Данная строка:\n{s}")

s = s.lower()
print(f"Строка, приведенная к нижнему регистру:\n{s}")

s = s.translate(str.maketrans('', '', string.punctuation))
print(f"Строка, без знаков пунктуации:\n{s}")

s = s.split(' ')
print(f"Список слов:\n{s}")

s_dict = dict(sorted(Counter(s).items(), key=lambda item: item[1], reverse=True))
print(f"Отсортированный словарь:\n{s_dict}")