def option1 (charSet):
    newList = charSet
    tempList = list()
    mixedList = list()
    num=0
    myWordlist = open(f"./custom_char_wl.txt", "w")
    while(num<len(charSet)):
        for i in newList:
            if i not in mixedList:
                mixedList.append(i)
                myWordlist.write(f'{i}\n')
            for j in charSet:
                tempList.append(i+j)
        newList=tempList
        tempList=list()
        num+=1
    myWordlist.close()

def option2 (charLen, charSet):
    myWordList = open("./custom_len_wl.txt", "w")
    word=""
    tempWord = list()
    for i in range(charLen):
        tempWord.append(0)
        word+=charSet[0]
    myWordList.write(f'{word}\n')
    while sum(tempWord) <= (len(charSet)-1)*charLen:
        if tempWord[charLen-1] < len(charSet)-1:
            tempWord[charLen-1]+=1
        else:
            tempWord[charLen-1] = 0
            for i in range(charLen-2, -1, -1):
                if tempWord[i] < len(charSet)-1:
                    tempWord[i]+=1
                    break
                else:
                    tempWord[i] = 0
        word = "" 
        for j in tempWord:
            word+=charSet[j]
        myWordList.write(f'{word}\n')
    myWordList.close()

def option3 (charSet):
    newList = charSet
    tempList = list()
    num=0
    myWordList = open("./max_limit_wl.txt", "w")
    while(num<len(charSet)):
        for i in newList:
            myWordList.write(f'{i}\n')
            for j in charSet:
                tempList.append(i+j)
        newList=tempList
        tempList=list()
        num+=1
    myWordList.close()

def option4(charSet, minLen, maxLen):
    newList = charSet
    tempList = list()
    num=0
    myWordList = open("./min_max_wl.txt", "w")
    while(num<len(charSet)):
        for i in newList:
            if len(i)<=maxLen and len(i)>=minLen:
                myWordList.write(f'{i}\n')
            elif len(i) > maxLen:
                break
            for j in charSet:
                tempList.append(i+j)
        newList=tempList
        tempList=list()
        num+=1
    myWordList.close()

def main ():
    charSet = list("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-,./';][<>?":|}{\\ """)
    while True:
        option = input("""1. Enter custom characters\n2. Enter a word length.\n3. Use pre-existing character set\n   (word length starts from 1 ends at 97)\n   (Choose wisely)\n4. Use <min> and <max> length\n5. Enter q to Exit!\n\n Option number: """)
        if option == "1":
            charSet = list(input("Enter characters (space will be considered a character): \n"))
            option1(charSet)

        elif option == "2":
            charLen = int(input("Enter desired word length: "))
            option2(charLen, charSet)
        
        elif option == "3":
            option3(charSet)
        
        elif option == "4":
            minLen = int(input("Enter <min> length: "))
            maxLen = int(input("Enter <max> length: "))
            option4(charSet, minLen, maxLen)

        elif option == "q":
            quit(f"\n\t====Thanks for using WORDLIST GENERATOR====\n")
        
        else:
            print("Choose a valid option!")


if __name__ == '__main__':
    print("""   
                █░█░█ █▀█ █▀█ █▀▄ █░░ █ █▀ ▀█▀  
                ▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ █ ▄█ ░█░  

             █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
             █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄         
    """)
    print("Before running this script, make sure that you have write permission.")
    print()
    main()



    