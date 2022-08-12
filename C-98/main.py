def countWords ():

    NoOfWords=  0
    a = str(input('Enter the File Name'))

    b=open(a , 'r')
    for i in b :
        words = i.split()
        NoOfWords = NoOfWords + len(words)

    print(NoOfWords)

countWords()

