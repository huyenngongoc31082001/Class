from nltk.corpus import PlaintextCorpusReader
import nltk
import numpy as np

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

f = open(r'C:\Users\Admin\Documents\Class\DataTrainFeature\Kinh doanh.txt', 'r')
kinhDoanhMatrix = np.array([[int(num) for num in line.split(' ')] for line in f])
f.close()

f = open(r'C:\Users\Admin\Documents\Class\DataTrainFeature\Phap luat.txt', 'r')
phapLuatMatrix = np.array([[int(num) for num in line.split(' ')] for line in f])
f.close()

f = open(r'C:\Users\Admin\Documents\Class\DataTrainFeature\Suc khoe.txt', 'r')
sucKhoeMatrix = np.array([[int(num) for num in line.split(' ')] for line in f])
f.close()

f = open(r'C:\Users\Admin\Documents\Class\DataTrainFeature\The thao.txt', 'r')
theThaoMatrix = np.array([[int(num) for num in line.split(' ')] for line in f])
f.close()

f = open(r'C:\Users\Admin\Documents\Class\DataTrainFeature\Vi tinh.txt', 'r')
viTinhMatrix = np.array([[int(num) for num in line.split(' ')] for line in f])
f.close()

numberKinhDoanh = len(dataKinhDoanh.fileids())
numberPhapLuat = len(dataPhapLuat.fileids())
numberSucKhoe = len(dataSucKhoe.fileids())
numberTheThao = len(dataTheThao.fileids())
numberViTinh = len(dataViTinh.fileids())
numberText = len(dataTrain.fileids())

pKinhDoanh = numberKinhDoanh / numberText
pPhapLuat = numberPhapLuat / numberText
pSucKhoe = numberSucKhoe /numberText
pTheThao = numberTheThao / numberText
pViTinh = numberViTinh / numberText

numWordOfKinhDoanh = 0
numWordOfPhapLuat = 0
numWordOfSucKhoe = 0
numWordOfTheThao = 0
numWordOfViTinh = 0
pXKinhDoanh = np.zeros(2500)
pXPhapLuat = np.zeros(2500)
pXSucKhoe = np.zeros(2500)
pXTheThao = np.zeros(2500)
pXViTinh = np.zeros(2500)

for i in range(len(kinhDoanhMatrix)):
    pXKinhDoanh[kinhDoanhMatrix[i][1]] += kinhDoanhMatrix[i][2]
    numWordOfKinhDoanh += kinhDoanhMatrix[i][2]

for i in range(len(phapLuatMatrix)):
    pXPhapLuat[phapLuatMatrix[i][1]] += phapLuatMatrix[i][2]
    numWordOfPhapLuat += phapLuatMatrix[i][2]

for i in range(len(sucKhoeMatrix)):
    pXSucKhoe[sucKhoeMatrix[i][1]] += sucKhoeMatrix[i][2]
    numWordOfSucKhoe += sucKhoeMatrix[i][2]

for i in range(len(theThaoMatrix)):
    pXTheThao[theThaoMatrix[i][1]] += theThaoMatrix[i][2]
    numWordOfTheThao += theThaoMatrix[i][2]

for i in range(len(viTinhMatrix)):
    pXViTinh[viTinhMatrix[i][1]] += viTinhMatrix[i][2]
    numWordOfViTinh += viTinhMatrix[i][2]


pXKinhDoanh = (pXKinhDoanh + 1) / (numWordOfKinhDoanh + 2500)
pXPhapLuat = (pXPhapLuat + 1) / (numWordOfPhapLuat + 2500)
pXSucKhoe = (pXSucKhoe + 1) / (numWordOfSucKhoe + 2500)
pXTheThao = (pXTheThao + 1) / (numWordOfTheThao + 2500)
pXViTinh = (pXViTinh + 1) / (numWordOfViTinh + 2500)

print(dictionary)




