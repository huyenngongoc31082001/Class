from nltk.corpus import PlaintextCorpusReader
import nltk

corpus_root  = r"C:\Users\Admin\Documents\Class\DataTrain"
corpus_root1 = r"C:\Users\Admin\Documents\Class\DataTrain\Kinh doanh"
corpus_root2 = r"C:\Users\Admin\Documents\Class\DataTrain\Phap luat"
corpus_root3 = r"C:\Users\Admin\Documents\Class\DataTrain\Suc khoe"
corpus_root4 = r"C:\Users\Admin\Documents\Class\DataTrain\The thao"
corpus_root5 = r"C:\Users\Admin\Documents\Class\DataTrain\Vi tinh"
file_pattern = r".*.txt"

dataTrain = PlaintextCorpusReader(corpus_root, file_pattern)
dataKinhDoanh = PlaintextCorpusReader(corpus_root1, file_pattern)
dataPhapLuat = PlaintextCorpusReader(corpus_root2, file_pattern)
dataSucKhoe = PlaintextCorpusReader(corpus_root3, file_pattern)
dataTheThao = PlaintextCorpusReader(corpus_root4, file_pattern)
dataViTinh = PlaintextCorpusReader(corpus_root5, file_pattern)

dictionary = []
freqWord = nltk.FreqDist(dataTrain.words()).most_common(2500)
for i in range(2500):
    dictionary.append(freqWord[i][0])

def writeFeature(data):
    for i in range(len(data.fileids())):
        genre = [(data.fileids()[i], word) for word in data.words(data.fileids()[i])]
        freq = nltk.ConditionalFreqDist(genre)
        for j in range(len(freq[data.fileids()[i]])):
            if (data.words(data.fileids()[i])[j] in dictionary):
                temp = str(i) + ' ' + str(dictionary.index(data.words(data.fileids()[i])[j])) \
                       + ' ' + str(freq[data.fileids()[i]][data.words(data.fileids()[i])[j]]) + '\n'

                if(data.fileids()[i].startswith('KD')):
                    location = r'C:\Users\Admin\Documents\Class\DataTrainFeature\Kinh doanh.txt'
                elif(data.fileids()[i].startswith('PL')):
                    location = r'C:\Users\Admin\Documents\Class\DataTrainFeature\Phap luat.txt'
                elif (data.fileids()[i].startswith('SK')):
                    location = r'C:\Users\Admin\Documents\Class\DataTrainFeature\Suc khoe.txt'
                elif (data.fileids()[i].startswith('TT')):
                    location = r'C:\Users\Admin\Documents\Class\DataTrainFeature\The thao.txt'
                else:
                    location = r'C:\Users\Admin\Documents\Class\DataTrainFeature\Vi tinh.txt'
                file = open(location, 'a')
                file.write(temp)
                file.close()

writeFeature(dataKinhDoanh)
writeFeature(dataPhapLuat)
writeFeature(dataSucKhoe)
writeFeature(dataTheThao)
writeFeature(dataViTinh)

