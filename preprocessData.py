from nltk.corpus import PlaintextCorpusReader
import preprocess

corpus_root = r"C:\Users\Admin\Documents\Class\TrainFull"
corpus_root1 = r"C:\Users\Admin\Documents\Class\DataTrain"
file_pattern = r".*.txt"
dataTrainRaw = PlaintextCorpusReader(corpus_root, file_pattern, encoding='utf-16')

for i in range(len(dataTrainRaw.fileids())):
    locationText = dataTrainRaw.fileids()[i]
    containText = dataTrainRaw.raw(dataTrainRaw.fileids()[i])
    containText = preprocess.preProcessText(containText)
    if (locationText.startswith('Kinh')):
        location = corpus_root1 + '\\' + locationText[0: 10] + '\\' + locationText[11:]
    elif(locationText.startswith('Phap')):
        location = corpus_root1 + '\\' + locationText[0: 9] + '\\' + locationText[10:]
    elif(locationText.startswith('Suc')):
        location = corpus_root1 + '\\' + locationText[0: 8] + '\\' + locationText[9:]
    elif(locationText.startswith('The')):
        location = corpus_root1 + '\\' + locationText[0: 8] + '\\' + locationText[9:]
    else:
        location = corpus_root1 + '\\' + locationText[0: 7] + '\\' + locationText[8:]
    containText = containText.encode('utf8')
    file = open(location, 'wb')
    file.write(containText)
    file.close()
