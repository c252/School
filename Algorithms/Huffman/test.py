from huffman import *

f = open("mobydick.txt", "rb")
with open("mobydick.txt") as f:
    raw_text = f.read()

text_dict = {}
mobydick_probs = {}

for word in raw_text:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

for i in text_dict.keys():
    mobydick_probs[i] = text_dict[i]

word_count = sum(text_dict.values())
for word in text_dict:
    text_dict[word] /= word_count

h = Huffman(text_dict)

cr = 0

for i in list(h.huffman_code.keys()):
    cr += mobydick_probs[i] * len(h.huffman_code[i])

print(cr)