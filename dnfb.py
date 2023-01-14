import yadisk
import datetime
import os

y = yadisk.YaDisk(token="y0_AgAAAAAiAPOmAAkAuwAAAADZsTiE4v3jZZT3QaOPZ4FwYty79atKgEs")

def uploadDisk():
    now = datetime.datetime.now()
    directory = '.\json'
    if y.check_token():
        if not y.is_dir(f"/json/{now.day}.{now.month}.{now.year}"):
            y.mkdir(f"/json/{now.day}.{now.month}.{now.year}")
            print(f"Папка /json/{now.day}.{now.month}.{now.year} создана")
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            y.upload(f"json/{filename}", f"/json/{now.day}.{now.month}.{now.year}/{filename}")
            
if __name__ == "__main__":
    uploadDisk()