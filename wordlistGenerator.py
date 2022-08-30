def main(charSet):
    baseList = charSet
    newList = baseList
    tempList = list()
    myWordList = open("./wordList.txt", "w")
    num=0
    while(num<len(baseList)):
        for i in newList:
            myWordList.write(f'{i}\n')
            for j in baseList:
                tempList.append(i+j)
        newList=tempList
        tempList=list()
        num+=1
    myWordList.close()


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
        elif option == "q":
            quit(f"             ====Thanks for using WORDLIST GENERATOR====")
        else:
            charSet = list("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-,./';][<>?":|}{\\ """)
        main(charSet)
    