import json 
import datetime
import yadisk
import os

y = yadisk.YaDisk(token="y0_AgAAAAAiAPOmAAkAuwAAAADZsTiE4v3jZZT3QaOPZ4FwYty79atKgEs")


def menu():
    mFlag = input("""Hey, I am a bot for filling the database in json file format of the form:
    - Proposal to be answered
    - Answer
    good cat scribblers <3 meows
    to start, enter one of the commands
    [*] grabbler, [*] clear (dev)\n
    """)
    check(mFlag)

def check(mFlag):
    if mFlag == "grabbler":
        grab()
    else:
        mFlag = input("""
    [-] Error…
    to start, enter one of the commands
    [*] grabbler, [*] clear (dev)\n
    """)
        check(mFlag)
        

def loadall(dir):
    now = datetime.datetime.now()
    directory = './json'

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            y.upload(f"json/{filename}", f"{dir}/{filename}")
            print(f"[+] File {now.day}.{now.month}.{now.year}.{now.microsecond}/{filename} load")
        else:
            print(f"[-] File {now.day}.{now.month}.{now.year}.{now.microsecond}/{filename} already loaded")
    print("[+] Succsess!")

def loadone(minname, dir):
    directory = './json'

    f = os.path.join(directory, minname)
    if os.path.isfile(f):
        y.upload(f"json/{minname}", f"{dir}/{minname}")
        print(f"[+] File {dir}/{minname} load")
    else:
        print(f"[-] File {dir}/{minname} already loaded")
    print("[+] Succsess!")


def flag(minname, dir):
    flag = input("Do you want to upload only last file? if yes then enter Y, otherwise n. Y/n: ")
    if flag == "Y":
        loadone(minname, dir)
    elif flag == "n":
        loadall(dir)
    else:
        print("[-] Error…")
        print("[?] try again…")
        uploadDisk(minname)

def uploadDisk(minname):
    now = datetime.datetime.now()
    print("|__________dump to json folder on yadisk__________|\n")
    if y.check_token():
        if not y.is_dir(f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}"):
            y.mkdir(f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}")
            dir = (f"/json/{now.day}.{now.month}.{now.year}.{now.microsecond}")
            print(f"[+] Dir /json/{now.day}.{now.month}.{now.year}.{now.microsecond} create\n")
        else:
            print(f"[-] Dir /json/{now.day}.{now.month}.{now.year}.{now.microsecond} already created\n")
            print("[?] try again…")
            uploadDisk()
    flag(minname, dir)

def save(messages):
    now = datetime.datetime.now()
    name = f"json/dump{now.microsecond}.json"
    minname = f"dump{now.microsecond}.json"
    with open(name, 'a') as file:
        json.dump(messages, file, indent=0, ensure_ascii=False)
        file.write('\n') 
        print("|_______________dump to json folder________________|\n")
        print("")
        print(f"[+] File {name} save\n")
    uploadDisk(minname)

def grab():
    messages = []
    n = int(input("[?] Enter number of iterations: "))
    i = 0

    while True:
        question = input('Proposal to be answered: ')
        answer =  input('Answer: ')
        messages.append({
            "question": question,
            "answer": answer
        })
        i += 1
        print("[+] number of iterations", i)
        if i == n:
            save(messages)
            break

if __name__ == "__main__":    
    menu()