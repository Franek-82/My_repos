import requests


def get_words_from_wiktionary(category):
    url = "https://en.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": "Category:{}".format(category),
        "cmlimit": "5000"
    }

    response = requests.get(url, params=params)
    data = response.json()

    words = [page["title"] for page in data["query"]["categorymembers"]]
    return words


# Пример получения слов из категории "Russian nouns"
words = get_words_from_wiktionary("Russian nouns")
print(words)
