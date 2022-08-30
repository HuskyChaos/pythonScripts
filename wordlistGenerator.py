def generateTextFile(uList):
    myWordList = open("./wordList.txt", "w")
    for i in uList:
        myWordList.write(f'{i}\n')
    myWordList.close()

def uniqueList(tempList):
    uList = list()
    for word in tempList:
        if word not in uList:
            uList.append(word)
    generateTextFile(uList)

def main(charSet, mode):
    baseList = charSet
    newList = baseList
    tempList = list()
    num=0

    if mode == 0:
        myWordList = open("./wordList.txt", "w")
        while(num<len(baseList)):
            for i in newList:
                myWordList.write(f'{i}\n')
                for j in baseList:
                    tempList.append(i+j)
            newList=tempList
            tempList=list()
            num+=1
        myWordList.close()        

    else:    
        mixedList = list()
        while(num<len(baseList)):
            for i in newList:
                mixedList.append(i)
                for j in baseList:
                    tempList.append(i+j)
            newList=tempList
            tempList=list()
            num+=1
        uniqueList(mixedList)

if __name__ == '__main__':
    print("""   
                █░█░█ █▀█ █▀█ █▀▄ █░░ █ █▀ ▀█▀  
                ▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ █ ▄█ ░█░  

             █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
             █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄         
    """)
    print("Before running this script, make sure that you have write permission.")
    print("Enter q if you wish to exit!")
    print()
    while True:
        option = input("Enter 1 to use your own letters or press Enter to use pre-existing wordlist: ")
        if option == "1":
            charSet = list(input("Enter characters without space:\n"))
            mode = 1
        elif option == "q":
            quit(f"             ====Thanks for using WORDLIST GENERATOR====")
        else:
            charSet = list("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-,./';][<>?":|}{\\ """)
            mode = 0
        main(charSet, mode)
    