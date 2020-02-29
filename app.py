import nltk
import json
from typing import List, Dict, Iterable

res = '{"val_one" : "1", "val_two" : "2", "body" : "Fibonacci numbers appear unexpectedly often in mathematics, so much so that there is an entire journal dedicated to their study, the Fibonacci Quarterly. Applications of Fibonacci numbers include computer algorithms such as the Fibonacci search technique and the Fibonacci heap data structure, and graphs called Fibonacci cubes used for interconnecting parallel and distributed systems."}'

data = json.loads(res)

lyrics = data["body"]

tokens = nltk.word_tokenize(lyrics)

tagged = nltk.pos_tag(tokens)

def nouns_list(tagged_tokens: list) -> list:
    nouns: list = []
    for pair in tagged_tokens:
            word: str = pair[0]
            pos: str = pair[1]
            if pos == 'NN' or pos == 'NNS':
                nouns.append(word)
    return nouns

def most_freq(iter: Iterable) -> any:
    counts: dict = {}
    for item in iter:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    highest_freq: int = 0
    for word, count in counts.items():
        if count > highest_freq:
            highest_freq = count
    for word, count in counts.items():
        if count == highest_freq:
            return word

print(most_freq(nouns_list(tagged))) # -> numbers
