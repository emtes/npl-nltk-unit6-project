from typing import List, Dict
from nltk.tag import pos_tag_sents
import nltk

input_s: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

input_s = input_s.decode(encoding='UTF-8')

s_tokens: list = nltk.word_tokenize(input_s)

s_tagged = pos_tag_sents(s_tokens)
print(s_tagged)
