import json 
import datetime
import yadisk
import os

y = yadisk.YaDisk(token="y0_AgAAAAAiAPOmAAkAuwAAAADZsTiE4v3jZZT3QaOPZ4FwYty79atKgEs")


def uploadDisk():
    now = datetime.datetime.now()
    directory = './json'
    if y.check_token():
        if not y.is_dir(f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}"):
            y.mkdir(f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}")
            print(f"[+] Dir /json/{now.day}.{now.month}.{now.year}.{now.microsecond} create")
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            y.upload(f"json/{filename}", f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}/{filename}")
            print(f"[+] File {now.day}.{now.month}.{now.year}.{now.microsecond}/{filename} create")

def save(messages):
    now = datetime.datetime.now()
    name = f"json/dump{now.microsecond}.json"
    with open(name, 'a') as file:
        json.dump(messages, file, indent=0, ensure_ascii=False)
        file.write('\n') 
    uploadDisk()


def grab():
    messages = []
    n = int(input("[?] Enter number of iterations: "))
    i = 0

    while True:
        question = input('Предложение на которое надо ответить: ')
        answer =  input('ОтВет: ')
        messages.append({
            "question": question,
            "answer": answer
        })
        i += 1
        print("[+] number of iterations", i)
        if i == n:
            save(messages)
            break
            
grab()