from gensim.parsing import strip_non_alphanum, split_alphanum, strip_short, strip_numeric
from pyvi import ViTokenizer

stopWords = []
file = open(r'C:\Users\Admin\Documents\Class\stopWords.txt', encoding='utf8')
readline = file.readlines()
file.close()
for i in range(len(readline)):
    #readline[i] = readline[i].replace(' ', '_')
    readline[i] = ViTokenizer.tokenize(readline[i])
    readlines = readline[i].split()
    #print(type(readlines), readlines)
    stopWords += readlines
def preProcessText(raw):
    raw = strip_non_alphanum(raw).lower().strip()  # loai bo nhung ki tu
    raw = split_alphanum(raw)  # tach tu
    raw = strip_short(raw, minsize=2)  # loai bo ki tu dung mot minh
    raw = strip_numeric(raw)   # loai bo so
    raw = ViTokenizer.tokenize(raw)   # ghep tu tieng viet
    raw = " ".join([word for word in raw.split() if word not in stopWords]) # loai bo stopword
    return raw
