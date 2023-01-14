import telebot
import json 
import datetime
import yadisk
import os

bot = telebot.TeleBot("5880749400:AAGryVcdNpj2BrMRBFkN48XY2NcVaWrR9GQ")
y = yadisk.YaDisk(token="y0_AgAAAAAiAPOmAAkAuwAAAADZsTiE4v3jZZT3QaOPZ4FwYty79atKgEs")

print("Bot start")
messages = []
storage = {}

def init_storage(user_id):
  storage[user_id] = dict(n=None, q=None, a=None)

def store_number(user_id, key, value):
  storage[user_id][key] = dict(value=value)

def get_val(user_id, key):
  return storage[user_id][key].get('value')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hey, I am a bot for filling the database in json file format of the form:\n- Proposal to be answered\n- Answer\ngood cat scribblers <3 meows\nto start, enter /grabber")

@bot.message_handler(commands=['grabber'])
def grab(message):
    init_storage(message.from_user.id)
    mes = bot.reply_to(message, "[?] Enter number of iterations: ")
    bot.register_next_step_handler(mes, que)

def queans(message):
    a = message.text
    store_number(message.from_user.id, "a", a)

    i = 0
    num = get_val(message.from_user.id, "n")
    ques = get_val(message.from_user.id, "q")
    answ = get_val(message.from_user.id, "a")

    while True:
        messages.append({
            "question": ques,
            "answer": answ
        })
        i += 1
        print("[+] number of iterations", i)
        if i == num:
            save(messages)
            break
        elif i != num:
            que(message)

def que(message):
    n = message.text

    question = bot.send_message(message.chat.id, 'Предложение на которое надо ответить: ')
    bot.register_next_step_handler(question, ans)
    store_number(message.from_user.id, "n", n)


def ans(message):
    q = message.text

    answer = bot.send_message(message.chat.id, 'ОтВет: ')
    bot.register_next_step_handler(answer, queans)
    store_number(message.from_user.id, "q", q)


def save(messages):
    now = datetime.datetime.now()
    name = f"json/dump{now.microsecond}.json"
    with open(name, 'a') as file:
        json.dump(messages, file, indent=0, ensure_ascii=False)
        file.write('\n') 
    uploadDisk()

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


            

bot.infinity_polling()



