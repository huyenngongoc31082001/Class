import numpy as np
from nltk.tokenize import word_tokenize
import caculate
import preprocess
from tkinter import *

def filterText(locationText):
    file = open(locationText, 'r', encoding='utf-8')
    contentText = file.read()
    file.close()
    #print(contentText)
    contentText = preprocess.preProcessText(contentText)
    vocabText = list(set(word_tokenize(contentText)))
    pKinhDoanhX = np.log(caculate.pKinhDoanh)
    pPhapLuatX = np.log(caculate.pPhapLuat)
    pSucKhoeX = np.log(caculate.pSucKhoe)
    pTheThaoX = np.log(caculate.pTheThao)
    pViTinhX = np.log(caculate.pViTinh)
    for i in range(2500):
        if(caculate.dictionary[i] in vocabText):
            pKinhDoanhX += np.log(caculate.pXKinhDoanh[i])
            pPhapLuatX += np.log(caculate.pXPhapLuat[i])
            pSucKhoeX += np.log(caculate.pXSucKhoe[i])
            pTheThaoX += np.log(caculate.pXTheThao[i])
            pViTinhX += np.log(caculate.pXViTinh[i])

    maxValue = max(pKinhDoanhX, pPhapLuatX, pSucKhoeX, pTheThaoX, pViTinhX)
    if(pKinhDoanhX == maxValue):
        return 'Kinh doanh'
    elif(pPhapLuatX == maxValue):
        return 'Pháp luật'
    elif(pSucKhoeX == maxValue):
        return 'Sức khỏe'
    elif(pTheThaoX == maxValue):
        return 'Thể thao'
    else:
        return 'Vi tính'


#print(filterText(r'C:\Users\Admin\Documents\Class\test.txt'))

root = Tk()
root.geometry("1400x700")


def remove_text():
    myLabel.config(text="")


def set_text():
    myLabel.config(text=filterText(r'C:\Users\Admin\Documents\Class\test.txt'))


def clear():
    my_text.delete(1.0, END)
    with open("test.txt", 'w', encoding='utf-8') as f:
        f.flush()
        f.write("")
        f.close()
    remove_text()


def get_text():
    string = my_text.get(1.0, END)
    with open("test.txt", 'w', encoding='utf-8') as f:
        f.flush()
        f.write(string)
        f.close()
    set_text()


my_text = Text(root, width=150, height=20, font=("helvetica", 13))
my_text.pack(pady=50)
button_frame = Frame(root)
button_frame.pack()
clear_button = Button(button_frame, text="NEW", command=clear)
clear_button.grid(row=0, column=1, padx=30)

run_button = Button(button_frame, text="RUN", command=get_text)
run_button.grid(row=0, column=0)
myLabel = Label(root, text="", font="BOLD")
myLabel.config(font=("helvetica", 20))
myLabel.place(x=700, y=600)
label1 = Label(root, text="Enter your test: ", font="BOLD").place(x=0, y=0)

root.mainloop()

#locationText = r'C:\Users\Admin\Documents\Class\test.txt'
#file = open(locationText, 'r', encoding='utf-8')
#contentText = file.read()
#file.close()
#print(contentText)
#print('Giá vàng trong nước - thế giới: Thu hẹp chênh lệch Giá vàng thế giới 635,5 USD'.encode())
