import difflib as df
txt1 = '''Приветствую stackoverflow. Есть два текстовых файла 1, 2.
 Я тут набросал работающий вариант, и мне в нем нравиться,
 что вывод игнорирует если строка в одном из файлов начинается
 с пробела или какой-либо вступительной фразы - выводит только совпадения.'''
txt2 = '''Приветствую сообщество stackoverflow. Есть два .. файла 1, 2.
 Я тут набросал .. вариант, и мне в нем нравиться,
 что вывод игнорирует если строка в одном из файлов начинается
 с пробела или какой-либо вступительной фразы - выводит только совпадения.'''
txt1_list = txt1.splitlines()
txt2_list = txt2.splitlines()

d = df.Differ()
diff = d.compare(txt1_list, txt2_list)
print('\n'.join(diff))