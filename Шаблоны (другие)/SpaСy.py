import spacy

nlp = spacy.load("ru_core_news_sm")  # Загрузка модели языка для русского

words = ["яблоко", "стол", "идти", "красный"]

nouns = []

for word in words:
    doc = nlp(word)
    for token in doc:
        if token.pos_ == "NOUN":  # Проверка, что слово является существительным
            nouns.append(word)

print(nouns)  # Вывод существительных
