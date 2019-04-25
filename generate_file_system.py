import os, random, time
from datetime import datetime
from pathlib import Path

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
    ret = []
    for _ in range(count):
        word_count = random.randint(1, 4)
        name_words = random.choices(words, k=word_count)
        ret.append(" ".join(name_words))
    return ret

def generate_files(destination, count=100, is_directory=False):
    file_names = generate_file_names(count)
    mod_times = generate_mod_time(count)
    for i in range(count):
        file_name = os.path.join(destination, file_names[i])
        mod_time = time.mktime(mod_times[i].timetuple())
        if is_directory:
            os.makedirs(file_name)
        else:
            file_name = "%s.txt" % file_name
            with open(file_name, "w") as f:
                f.write("")
        os.utime(file_name, (mod_time, mod_time))
        print("Generated file:", file_name)
    

if __name__ == '__main__':
    default_dir = os.path.join(Path.home(), "Documents/test_directory")
    generate_files(default_dir)