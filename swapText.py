def swapText():
    with open('textFile1.txt','r') as a:
        data_1 = a.read()
    with open('textFile2.txt','r') as b:
        data_2 = b.read()
    with open('textFile1.txt','w') as a:
        a.write(data_2)
    with open('textFile2.txt','w') as b:
        b.write(data_1)
swapText()