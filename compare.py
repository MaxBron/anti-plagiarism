import codecs
import sys
import ast


# расстояние Левенштейна
def levenstein(str_1, str_2):
    l, m = len(str_1), len(str_2)  # длины текстов
    if l > m:
        str_1, str_2 = str_2, str_1
        l, m = m, l
    current_row = range(l + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * l
        for j in range(1, l + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[l]


input_file = open(sys.argv[1])
scores_file = open(sys.argv[2], 'w')
for line in input_file:
    text_file = codecs.open(line.split()[0], "r", encoding="utf-8")
    text = text_file.read()
    text_file.close()
    text_file = codecs.open(line.split()[1], "r", encoding="utf-8")
    text_1 = text_file.read()
    text_file.close()
    text, text_1 = ast.parse(text), ast.parse(text_1)      # предобработка текстов
    text, text_1 = ast.unparse(text), ast.unparse(text_1)  #
    scores_file.write(str(round(1 - (levenstein(text, text_1) / (max(len(text), len(text_1)))), 2)) + '\n')
scores_file.close()
input_file.close()
