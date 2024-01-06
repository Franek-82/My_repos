import csv

with open("C:/Python/Частотный словарь/111.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter="\t")
    for el in reader:
        print(el[0])
