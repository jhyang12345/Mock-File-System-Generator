import os, random

# works only in unix systems
def read_words():
    words = []
    with open("/usr/share/dict/words", "r") as f:
        words = f.read().split()
    return words

def generate_file_names(count=100):
    words = read_words()
    for _ in range(count):
        word_count = random.randint(1, 4)
        name_words = random.choices(words, k=word_count)
        print(name_words)

if __name__ == '__main__':
    generate_file_names()