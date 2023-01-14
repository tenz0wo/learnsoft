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
    array_q = []
    array_a = []

    n = int(input("[?] Enter number of iterations: "))
    i = 0

    for i in range(n):
        question = input('Предложение на которое надо ответить: ')
        array_q.append(question)
        answer =  input('ОтВет: ')
        array_a.append(answer)
        i += 1
        print("[+] number of iterations", i)

    print(array_q, array_a)
    messages.append({
        "question": array_q,
        "answer": array_a
    })
    print(messages)
    i = 0
    for i in messages:
        for j in question:
            for k in answer:
                print(j, question)
                print(k, answer)
                i =+ 1
               
       
        
        
            
grab()