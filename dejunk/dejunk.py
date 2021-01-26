"""Main module."""


with open("configs/test.txt", 'r') as f:
    ls = [text.strip() for text in f.readlines() if '#' not in text]
    print(ls)
