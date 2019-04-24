import os, random, time
from datetime import datetime

def generate_mod_time(count=100, start='2017-01-01', end=None):
    start_time = time.mktime(datetime.strptime(start, "%Y-%m-%d").timetuple())
    end_time = None
    if not end:
        end_time = int(datetime.now().strftime("%s"))
    else:
        end_time = time.mktime(datetime.strptime(end, "%Y-%m-%d").timetuple())
    diff = end_time - start_time
    ret = []
    for _ in range(count):
        roulette = random.random() * diff
        date = datetime.fromtimestamp((start_time + int(roulette)))
        ret.append(date)
    return ret
            
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
    generate_mod_time()