import csv

with open("C:/Python/Частотный словарь/freqrnc2011.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter="\t")
    li = []
    for row in reader:
        if row[1] == "s" and float(row[2]) > 0.9 and len(row[0]) > 1:
            li.append(row[0])
print(len(li))  # 14557
with open("C:/Python/Частотный словарь/my_nouns.txt", "w", encoding='utf-8') as f:
    f.writelines(line + "\n" for line in li)
    #  использовал генератор для сохранения \n
