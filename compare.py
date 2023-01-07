import codecs
import sys
import ast


# расстояние Левенштейна
def levenstein(text_1, text_2):
    l, m = len(text_1), len(text_2)  # длины текстов
    if l > m:
        text_1, text_2 = text_2, text_1
        l, m = m, l
    current_row = range(l + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * l
        for j in range(1, l + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if text_1[j - 1] != text_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[l]


input_file = open(sys.argv[1])
scores_file = open(sys.argv[2], 'w')
for line in input_file:
    text_file = codecs.open(line.split()[0], "r", encoding="utf-8")
    text_1 = text_file.read()
    text_file.close()
    text_file = codecs.open(line.split()[1], "r", encoding="utf-8")
    text_2 = text_file.read()
    text_file.close()
    text_1, text_2 = ast.parse(text_1), ast.parse(text_2)      # предобработка текстов
    text_1, text_2 = ast.unparse(text_1), ast.unparse(text_2)  #
    scores_file.write(str(round(1 - (levenstein(text_1, text_2) / (max(len(text_1), len(text_2)))), 2)) + '\n')
scores_file.close()
input_file.close()
