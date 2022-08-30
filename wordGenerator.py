def main(charSet):
    baseList = charSet
    newList = baseList
    tempList = list()
    print(baseList)
    num=0
    while(num<len(baseList)):
        for i in newList:
            print(i)
            for j in baseList:
                tempList.append(i+j)
        newList=tempList
        tempList=list()
        num+=1


if __name__ == '__main__':
    option = input("Enter 1 to use your own letters or press Enter to use pre-existing wordlist: ")
    if option == "1":
        charSet = list(input("Enter characters without space:\n"))
    else:
        charSet = list("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-,./';][<>?":|}{\\""")
    main(charSet)
    