#!/usr/bin/python3

def ones(x):
    wl = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return wl[x]

def special(x):
    wl = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return wl[x]

def tens(x):
    wl = ["", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if x == 0:
        return wl[0]
    else:
        return wl[x-1]

def main():
    inputNumber = input("Enter a number: ")
    # print(f'Enter number: {x}')
    # inputNumber = x
    inputNumber = inputNumber[::-1]

    ans = list()

    for i in range(len(inputNumber)):
        if i == 0:
            ans.append(ones((int(inputNumber[i]))))
        elif i == 1:
            if inputNumber[i] == "1":
                ans.remove(ans[i-1])
                ans.append(special(int(inputNumber[i-1])))
            else:
                if ans[i-1] == "Zero":
                    ans.remove(ans[i-1])
                ans.append(tens(int(inputNumber[i])))
        elif i == 2:
            ans.append("Hundred")
            ans.append(ones(int(inputNumber[i])))
        elif i == 3:
            ans.append("Thousand")
            ans.append(ones(int(inputNumber[i])))
        elif i == 4:
            if inputNumber[i] == "1":
                ans.remove(ans[i-1])
                ans.append(special(int(inputNumber[i-1])))
            else:
                if ans[i-1] == "Zero":
                    ans.remove(ans[i-1])
                ans.append(tens(int(inputNumber[i])))

    print(list(reversed(ans)))
    # print(" ".join(list(reversed(ans))))


if __name__ == "__main__":
    while True:
        main()
