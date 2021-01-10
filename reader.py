import re
from spellchecker import SpellChecker

sp = SpellChecker()


def read_text():
    with open("text.txt", "r", encoding='utf-8') as f:
        return f.readlines()


def find_mistakes(words):
    miss = sp.unknown(words)
    for w in miss:
        sp.candidates(w)
    return miss


def get_text():
    text = read_text()
    words = []
    for i in range(0, len(text)):
        text[i] = text[i].replace('\n', '').replace('–', '-')
        text[i] = re.sub(r"[^\w\s\.-]", '', text[i], re.UNICODE)
        words += [word.strip('.') for word in text[i].split(" ")]
    return list(set(words))
